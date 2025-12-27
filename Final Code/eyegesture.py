import cv2
import mediapipe as mp
import pyttsx3
import serial
import time
import numpy as np

# Serial setup (update COM port if needed)
arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

# Voice feedback
engine = pyttsx3.init()
def speak(cmd):
    engine.say(cmd)
    engine.runAndWait()

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

# Command map
command_values = {
    "RIGHT": 1,
    "LEFT": 2,
    "FORWARD": 3,
    "BACKWARD": 4,
    "STOP": 5
}

# Blink and debounce
blink_counter = 0
blink_threshold = 5
last_command = ""
last_time = time.time()

# Eye calibration data
calibration_data = {
    "LEFT": None,
    "RIGHT": None,
    "UP": None,
    "NEUTRAL": None
}
calibrated = False

# Eye landmarks for pupils
LEFT_PUPIL = 468
RIGHT_PUPIL = 473

# Calibration function
def calibrate_position(label, timeout=4):
    print(f"Look {label} for {timeout} seconds...")
    coords = []

    start_time = time.time()
    while time.time() - start_time < timeout:
        ret, frame = cap.read()
        if not ret:
            continue
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(frame_rgb)
        if results.multi_face_landmarks:
            mesh = results.multi_face_landmarks[0].landmark
            left_pupil = mesh[LEFT_PUPIL]
            right_pupil = mesh[RIGHT_PUPIL]
            coords.append([(left_pupil.x + right_pupil.x) / 2, (left_pupil.y + right_pupil.y) / 2])
        cv2.putText(frame, f"Calibrating: Look {label}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Calibration", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    if coords:
        calibration_data[label] = np.mean(coords, axis=0)
        print(f"{label} position calibrated:", calibration_data[label])

# Command sender with debouncing
def send_command(cmd):
    global last_command, last_time
    if cmd != last_command and (time.time() - last_time) > 1.5:
        value = command_values.get(cmd, 0)
        if value != 0:
            arduino.write(f"{value}\n".encode())
            print(f"Sent: {cmd} ({value})")
            speak(cmd)
            last_command = cmd
            last_time = time.time()

# Start webcam
cap = cv2.VideoCapture(0)

# Calibration phase
for direction in ["NEUTRAL", "LEFT", "RIGHT", "UP"]:
    calibrate_position(direction)
cv2.destroyAllWindows()
calibrated = all(v is not None for v in calibration_data.values())

if not calibrated:
    print("Calibration failed. Exiting.")
    cap.release()
    arduino.close()
    exit()

# Thresholds
POSITION_TOLERANCE = 0.02
EYE_OPEN_THRESHOLD = 0.015

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        mesh = results.multi_face_landmarks[0].landmark
        left_pupil = mesh[LEFT_PUPIL]
        right_pupil = mesh[RIGHT_PUPIL]

        # Blink detection
        eye_top = mesh[159].y
        eye_bottom = mesh[145].y
        eye_open = eye_bottom - eye_top

        if eye_open < EYE_OPEN_THRESHOLD:
            blink_counter += 1
        else:
            if 1 <= blink_counter <= blink_threshold:
                send_command("STOP")
            elif blink_counter > blink_threshold:
                send_command("BACKWARD")
            blink_counter = 0

        # Gaze detection using Euclidean distance
        pupil_avg = np.array([(left_pupil.x + right_pupil.x) / 2, (left_pupil.y + right_pupil.y) / 2])
        distances = {key: np.linalg.norm(pupil_avg - np.array(calibration_data[key])) for key in calibration_data}

        # Find closest match
        command = min(distances, key=distances.get)
        if distances[command] < POSITION_TOLERANCE:
            send_command(command)

    cv2.imshow("Eye Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

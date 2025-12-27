**👁️ Eye Gesture Communication System for Assistive Control**
**🧠 Project Overview**

The Eye Gesture Communication System is an assistive technology solution designed to help individuals with severe motor disabilities communicate and control devices using only eye movements and blink gestures.
The system leverages computer vision and real-time eye tracking to interpret gaze directions and blink patterns, converting them into meaningful commands with visual and voice feedback.

This project focuses on accuracy, affordability, and real-world usability, making it suitable for applications such as assistive communication, robotic control, and wheelchair navigation.

**🎯 Objectives**

Enable hands-free communication and control using eye gestures

Accurately detect both eye pupils together (not separately)

Convert gaze and blink gestures into clear control commands

Provide real-time visual and voice feedback

Integrate seamlessly with Arduino hardware for physical movement

Ensure low-cost and accessible implementation

**🚀 Key Features**
**👀 Eye Tracking & Gesture Detection**

Real-time eye tracking using MediaPipe Face Mesh & Iris landmarks

Tracks both pupils together for higher stability and accuracy

Detects:

Left gaze

Right gaze

Upward gaze

Neutral position

Single blink

Double blink

**🧭 Gesture-to-Command Mapping**
Eye Gesture	Command
Look Left	MOVE LEFT
Look Right	MOVE RIGHT
Look Up	MOVE FORWARD
Look Down / Blink Pattern	MOVE BACKWARD
Single Blink	STOP
Double Blink	CONFIRM / ACTIVATE
**🔊 Voice Feedback**

Uses Text-to-Speech (pyttsx3) to announce detected commands

Helps users confirm actions without visual dependency

**🖥️ On-Screen Display**

Displays:

Detected eye position

Current command

Eye landmarks and pupil tracking

Real-time feedback for debugging and calibration

**⚙️ Hardware Integration**

Sends control signals to Arduino Uno via serial communication

Controls:

Servo motors (LEFT / RIGHT)

DC motors (FORWARD / BACKWARD)

Designed for:

Wheelchair control

Robotic navigation

Assistive mobility systems

**🧪 Calibration & Accuracy**

Includes an initial calibration phase to adapt to individual eye movement patterns

Personalized threshold values for:

Horizontal gaze

Vertical gaze

Blink duration

Reduces false detections and repeated commands

Ensures smooth and reliable real-time performance

**🛠️ Technologies Used
Software**

Python

OpenCV

MediaPipe (Face Mesh & Iris Tracking)

NumPy

pyttsx3 (Text-to-Speech)

PySerial

Hardware

Arduino Uno

Servo Motor

DC Motors

Motor Driver Module

USB Camera / Laptop Camera


**⚙️ Installation & Setup**
1️⃣ Clone the Repository
git clone https://github.com/your-username/eye-gesture-communication-system.git
cd eye-gesture-communication-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Arduino Setup

Upload the Arduino sketch to control motors and servos

Connect Arduino via USB

Ensure correct COM port is selected in Python code

4️⃣ Run the Application
python eye_gesture_control.py

**🧩 Use Cases**

Assistive communication for people with motor disabilities

Wheelchair control using eye gestures

Hands-free robotic control

Human–computer interaction research

Healthcare and rehabilitation systems

**🌟 Future Enhancements**

GUI dashboard for easier configuration

Machine learning-based adaptive gesture learning

Mobile camera integration

Wireless (Bluetooth/Wi-Fi) Arduino communication

Emergency alert system using eye gestures

📸 Demo

🎥 Demo videos and screenshots are available in the assets/ folder.

**👤 Created By**

Deenadayalan R
👨‍💻 AI | Computer Vision | Assistive Technology Enthusiast

LinkedIn: https://www.linkedin.com/in/deenadayalan-r-370359250/

GitHub: https://github.com/Candydeena?tab=repositories

📜 License

This project is developed for educational and assistive research purposes.
You are free to use and modify it with proper attribution.

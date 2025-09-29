# AI Virtual Mouse with Gesture-Based Volume Control
  _Computer Vision Project

This project implements a hand gesture–controlled virtual mouse with additional features for scrolling and volume adjustment. It is designed as a computer vision project, combining real-time hand tracking with desktop automation libraries to enable natural human–computer interaction using a standard webcam. A Tkinter-based graphical interface is also included for ease of use.

 _Project Structure

├── ai_virtual_mouse_project_scroll_volume.py   
├── gui.py                                      
├── hand_module.py                              
└── README.md                                   

# Features

Control the mouse cursor using hand gestures
Perform left-click using an index–middle finger pinch gesture
Adjust system volume using the distance between the thumb and index finger
Scroll through content by vertical hand movement
Real-time visual feedback on the webcam feed
Graphical interface for starting, stopping, and displaying instructions

# Requirements

The following Python packages are required to run the project:

opencv-python
numpy
autopy
pyautogui
comtypes
pycaw
mediapipe
tkinter   

# Installation

Clone the repository and install the required dependencies:

git clone https://github.com/your-username/ai-virtual-mouse-volume-cv.git
cd ai-virtual-mouse-volume-cv
pip install -r requirements.txt

If you prefer not to use a requirements.txt, install manually:
pip install opencv-python numpy autopy pyautogui comtypes pycaw mediapipe

# Usage

Run the project with the graphical interface:
python gui.py
Run the core virtual mouse functionality directly:
python ai_virtual_mouse_project_scroll_volume.py
Exit the program at any time by pressing the Q key while the webcam window is active.

# Gesture Controls

Mouse movement: Raise the index finger
Left click: Raise both the index and middle fingers and bring them together
Volume adjustment: Raise the thumb and index finger, then vary the distance between them
Scrolling: Raise four fingers (excluding the pinky) and move the index finger vertically

# File Overview

ai_virtual_mouse_project_scroll_volume.py
Implements the core logic for gesture detection, mouse control, scrolling, and volume adjustment. Provides real-time feedback on the webcam feed.
gui.py
Implements a Tkinter-based user interface with buttons to start the virtual mouse, view instructions, and exit the program.
hand_module.py
Implements a wrapper around Mediapipe for hand detection. Provides methods for identifying hand landmarks, determining finger states, and calculating distances between landmarks.

# Troubleshooting

If the webcam feed does not appear, change the camera index in cv2.VideoCapture(0) to cv2.VideoCapture(1) or higher
If cursor movement feels delayed, adjust the smoothening parameter in the code
If scrolling is too sensitive or too slow, modify the scroll_sensitivity variable
If volume control does not work, verify that the system audio devices are properly configured. Note that PyCaw works only on Windows

# Compatibility

Windows 10 and Windows 11: Fully supported, including volume control
Linux and macOS: Core virtual mouse features (cursor, click, and scroll) should work, but volume control is not supported

# Future Improvements

Support for right-click and double-click gestures
Multi-hand gesture support
Cross-platform implementation of volume control
Customizable gesture-to-action mapping through the GUI

# Author
This project was developed as an applied Computer Vision project, combining real-time hand tracking with desktop automation and control.

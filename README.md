# Hands-Free Interactive System

## Overview
This project implements an eye-controlled mouse and voice typing system using Python. It leverages computer vision to track eye movements and control the mouse cursor, while also allowing users to input text through voice commands. The system is designed to assist users with disabilities or those who prefer hands-free interaction with their computers.

## Components
The project consists of three main components:

1. **MouseControl**: This module handles the camera input and processes the eye movements to control the mouse cursor. It uses OpenCV and MediaPipe for real-time face and landmark detection.

2. **VoiceTyping**: This module captures voice input using the SpeechRecognition library and translates it into text commands. It can also trigger mouse actions based on recognized commands.

3. **Main Application**: The main script that initializes the MouseControl and VoiceTyping classes, manages threading for mouse control, and listens for voice commands in a loop.

## Installation
To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required packages**:
   Make sure you have Python installed (preferably Python 3.6 or higher). Then, install the required libraries using pip:
   ```bash
   pip install opencv-python mediapipe pyautogui SpeechRecognition
   ```

3. **Set up microphone permissions**:
   Ensure that your microphone is accessible by the application. You may need to adjust your system settings to allow microphone access.

## Usage
1. **Run the application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Voice Commands**:
   - **Click**: Triggers a mouse click at the current cursor position.
   - **Scroll up**: Scrolls the page up.
   - **Scroll down**: Scrolls the page down.
   - **Pause**: Pauses the mouse control.
   - **Resume**: Resumes the mouse control.
   - **Delete**: Stops all processes and exits the application.

3. **Eye Control**:
   The application will use your webcam to track your eye movements. Ensure that you are positioned correctly in front of the camera for optimal performance.

## Code Structure
- `main.py`: The entry point of the application that initializes and runs the mouse control and voice typing functionalities.
- `mouse_control.py`: Contains the `MouseControl` class responsible for capturing video input and controlling the mouse based on eye movements.
- `voice_typing.py`: Contains the `VoiceTyping` class that handles voice recognition and command processing.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- [OpenCV](https://opencv.org/) for computer vision capabilities.
- [MediaPipe](https://mediapipe.dev/) for face and landmark detection.
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) for simulating mouse and keyboard actions.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for voice command processing.

# Eye Controlled Mouse
Description

The Eye Controlled Mouse is an innovative project that utilizes computer vision and machine learning to enable hands-free control of a computer mouse using eye movements. By leveraging the power of OpenCV, MediaPipe, and PyAutoGUI, this project tracks facial landmarks and translates them into cursor movements and clicks, providing an alternative method of computer interaction for users with limited mobility or those seeking a touchless interface.

Features

Real-Time Face and Eye Tracking: Uses MediaPipe Face Mesh to detect and track facial landmarks in real-time.

Cursor Control: Moves the mouse cursor based on the position of the user's eyes.

Click Detection: Simulates mouse clicks when the user blinks, offering a hands-free clicking mechanism.

Interactive GUI: Displays the camera feed with visual indicators for detected landmarks and cursor positions.

Technologies Used

OpenCV: For video capture and image processing.

MediaPipe: For face and eye landmark detection.

PyAutoGUI: For controlling the mouse cursor and simulating clicks.

How It Works

Video Capture: The webcam captures the video feed, which is then processed frame by frame.

Face Mesh Detection: MediaPipe's Face Mesh model detects facial landmarks, with refined landmarks around the eyes.

Landmark Processing: The coordinates of specific eye landmarks are used to calculate the cursor position on the screen.

Cursor Movement: PyAutoGUI moves the cursor to the calculated position.

Click Simulation: Detects blinks by measuring the distance between specific eye landmarks and simulates a mouse click.

Accomplishments

Successfully implemented real-time eye tracking using MediaPipe's Face Mesh.

Achieved smooth and accurate cursor control based on eye movements.

Developed a reliable blink detection mechanism for simulating mouse clicks.

Created an interactive GUI that visualizes the tracking process and cursor movements.

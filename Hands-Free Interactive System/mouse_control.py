import cv2
import mediapipe as mp
import pyautogui
import threading

class MouseControl:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        self.screen_w, self.screen_h = pyautogui.size()
        self.is_paused = False  # Flag to control pause/resume

    def run(self):
        while True:
            if not self.is_paused:  # Only process if not paused
                _, frame = self.cam.read()
                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                output = self.face_mesh.process(rgb_frame)
                landmark_points = output.multi_face_landmarks
                frame_h, frame_w, _ = frame.shape

                if landmark_points:
                    landmarks = landmark_points[0].landmark
                    for id, landmark in enumerate(landmarks[474:478]):
                        x = int(landmark.x * frame_w)
                        y = int(landmark.y * frame_h)
                        cv2.circle(frame, (x, y), 3, (0, 255, 0))
                        if id == 1:
                            screen_x = int(self.screen_w * landmark.x)
                            screen_y = int(self.screen_h * landmark.y)
                            current_x, current_y = pyautogui.position()
                            smooth_x = int(current_x + (screen_x - current_x) * 0.1)
                            smooth_y = int(current_y + (screen_y - current_y) * 0.1)
                            pyautogui.moveTo(smooth_x, smooth_y)

                    left = [landmarks[145], landmarks[159]]
                    for landmark in left:
                        x = int(landmark.x * frame_w)
                        y = int(landmark.y * frame_h)
                        cv2.circle(frame, (x, y), 3, (0, 255, 255))

                    if (left[0].y - left[1].y) < 0.01:
                        pyautogui.click()
                        pyautogui.sleep(1)

                cv2.imshow('Eye Controlled Mouse', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                    break
            else:
                cv2.waitKey(100)  # Wait a bit while paused

        self.cam.release()  # Release the camera
        cv2.destroyAllWindows()  # Close all OpenCV windows

    def click(self):
        pyautogui.click()  # Simulate a mouse click

    def scroll_up(self):
        pyautogui.scroll(10)  # Scroll up

    def scroll_down(self):
        pyautogui.scroll(-10)  # Scroll down

    def pause(self):
        self.is_paused = True  # Set the pause flag

    def resume(self):
        self.is_paused = False  # Clear the pause flag

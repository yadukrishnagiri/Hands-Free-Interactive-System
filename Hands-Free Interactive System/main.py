from mouse_control import MouseControl
from voice_typing import VoiceTyping
import cv2

def main():
    mouse_control = MouseControl()
    voice_typing = VoiceTyping()

    # Start mouse control in a separate thread
    import threading
    mouse_thread = threading.Thread(target=mouse_control.run)
    mouse_thread.start()

    while True:
        # Get voice input
        recognized_text = voice_typing.listen()
        print("Recognized Text:", recognized_text)

        # Check for commands to control mouse actions or pause/resume
        if recognized_text.lower() == "delete":
            print("Stopping all processes...")
            break  # Exit the loop to stop the camera
        elif recognized_text.lower() == "pause":
            mouse_control.pause()  # Pause mouse control
            print("Mouse control paused.")
        elif recognized_text.lower() == "resume":
            mouse_control.resume()  # Resume mouse control
            print("Mouse control resumed.")

    # Clean up
    mouse_control.cam.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows
    mouse_thread.join()  # Wait for the mouse control thread to finish

if __name__ == "__main__":
    main()
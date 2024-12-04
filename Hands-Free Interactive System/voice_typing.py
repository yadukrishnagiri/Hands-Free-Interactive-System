import speech_recognition as sr
import pyautogui  # Import pyautogui for keyboard simulation
from mouse_control import MouseControl  # Import MouseControl to access its methods

class VoiceTyping:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mouse_control = MouseControl()  # Create an instance of MouseControl

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            print("Audio captured.")
            try:
                text = self.recognizer.recognize_google(audio)
                print("Recognized text:", text)
                self.handle_command(text)  # Call the new method to handle commands
                return text
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return "Could not understand audio."
            except sr.RequestError as e:
                print(f"Error: {e}")
                return f"Error: {e}"

    def handle_command(self, command):
        command = command.lower()
        if "click" in command:
            self.mouse_control.click()  # Call the click method in MouseControl
        elif "scroll up" in command:
            self.mouse_control.scroll_up()  # Call the scroll up method in MouseControl
        elif "scroll down" in command:
            self.mouse_control.scroll_down()  # Call the scroll down method in MouseControl
        else:
            self.type_text(command)  # Default to typing text

    def type_text(self, text):  # New method to simulate keyboard input
        pyautogui.write(text)  # Simulate typing the recognized text

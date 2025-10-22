import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

def processcommand(command):
    print(f"Processing command: {command}")
    # You can add actual command handling here

if __name__ == "__main__":
    speak("Initializing Alfred...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)
                print(f"You said: {word}")

            if word.lower() == "alfred":
                try:
                    speak("Yes?")
                except Exception as e:
                    print(f"Speech error: {e}")

                time.sleep(0.5)

                with sr.Microphone() as source:
                    print("Alfred active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")

                processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"Error: {e}")
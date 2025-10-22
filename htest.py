import pyttsx3

engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  # Try voices[1] if needed

engine.say("This is a test of your audio system.")
engine.runAndWait()
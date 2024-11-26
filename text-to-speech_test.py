import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_text(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Start voice recognition
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Listening... Speak something!")

    try:
        # Listen and process audio
        audio = recognizer.listen(source)
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")

        # Respond with TTS
        response = f"You just said: {command}. How can I assist you further?"
        speak_text(response)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        speak_text("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")
        speak_text("There seems to be an issue with the internet connection.")

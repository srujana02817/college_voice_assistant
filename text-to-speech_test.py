import speech_recognition as sr
import pyttsx3
import spacy
from textblob import TextBlob


# Initialize recognizer and TTS engine and NLP model
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = spacy.load("en_core_web_sm")

def speak_text(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def extract_entities(command):
    """Extract key entities from the command."""
    doc = nlp(command)
    entities = [ent.text for ent in doc.ents if ent.label_ in [""" Entities from the database """]]
    return entities

def analyze_sentiment(command):
    """Analyze the sentiment of the command(optional)."""
    blob = TextBlob(command)
    return blob.sentiment.polarity

def interpret_command(command):
    """Interpret user command and return appropriate response."""
    doc = nlp(command.lower())
    
    if "department" in command:
        return "Let me find the department you're looking for."
    elif any(word in command for word in ["faculty", "professor", "teacher"]):
        return "I will provide details about the faculty."
    elif "principal" in command:
        return "The principal's office is in Block A."
    elif any(word in command for word in ["library", "libra"]):
        return "The library is on the second floor."
    elif "event" in command:
        return "The next event is scheduled for March 2024."
    elif doc.ents and any(ent.label_ == "PERSON" for ent in doc.ents):
        return f"I will find information about {doc.ents[0].text}."
    elif TextBlob(command).sentiment.polarity < 0:
        return "I'm here to help. How can I assist you further?"
    else:
        return "I'm not sure about that. Let me check."


def test_commands(command_list):
    for command in command_list:
        print(f"User Command: {command}")
        response = interpret_command(command)
        print(f"Response: {response}\n")

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

        # Respond with NLP
        response = interpret_command(command)
        print(f"Response : {response}")
        speak_text(response)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        speak_text("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")
        speak_text("There seems to be an issue with the internet connection.")


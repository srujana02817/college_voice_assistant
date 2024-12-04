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
    """Generate a response based on the extracteed entities."""
    entities = extract_entities(command)
    if "" in command.lower():
        if entities :
            return f"Let me find the {entities[0]} nameeee "
        else :
            return "Which department would you like to find ?"
    return "I'm not sure how to help with that . Can you repharse ?"

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

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties
engine.setProperty('rate', 150)  # Speed (words per minute)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Speak a sample text
engine.say("Hello Samruddhi! Your voice assistant is ready to help.")
engine.runAndWait()

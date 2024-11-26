import speech_recognition as sr

#Initialize the recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise ... Please wait.")
    recognizer.adjust_for_ambient_noise(source,duration=2)
    print("Listening ... Speak Something!")

    try:
        #Caputure audio and recognize speech
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Could not request results. Check your internet Connection.")
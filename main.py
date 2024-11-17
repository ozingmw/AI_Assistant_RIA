import speech_recognition as sr
import pyttsx3
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

def process_command(command):
    tokens = word_tokenize(command)
    tokens = [word for word in tokens if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    print(f"Processed command: {filtered_tokens}")
    return filtered_tokens

def respond(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    while True:
        command = recognize_speech()
        if command:
            processed_command = process_command(command)
            respond("I have processed your command.")

if __name__ == "__main__":
    main()

import speech_recognition as sr   # Used to listen to your voice and convert it into text
import webbrowser                 # To open websites in your browser
import pyttsx3                    # To convert text into speech (computer talks)
import musicLibrary               # Your custom music library (You must create or define this module)
import requests                   # To send requests to websites (used here to get news)
from openai import OpenAI         # To connect with OpenAI API (for ChatGPT responses)
from gtts import gTTS             # Google’s Text-to-Speech for better voice output
import pygame                     # To play audio files
import os                         # To work with files and folders

recognizer = sr.Recognizer()      # Helps in converting voice to text
engine = pyttsx3.init()           # Initializes text-to-speech system (pyttsx3)
newsapi = "0de954be96de426da0877b4ec86973c5"  # API key for getting news from NewsAPI.org

# This is an old speak function using pyttsx3 (you’re not using this anymore)
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# New speak function → uses gTTS and pygame to speak
def speak(text):
    tts = gTTS(text)             # Converts the text to an mp3 file using Google’s TTS
    tts.save('temp.mp3')         # Saves the spoken output as a file

    pygame.mixer.init()          # Start Pygame’s audio system
    pygame.mixer.music.load('temp.mp3')   # Load that mp3 file
    pygame.mixer.music.play()    # Play the file

    # Wait here until the file finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()  # Free up resources
    os.remove("temp.mp3")        # Delete the mp3 file after playing

# This function sends your command to OpenAI (ChatGPT) and gets a reply
def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content  # Returns ChatGPT’s response text

# This function handles the tasks based on your spoken command
def processCommand(c):
    if "open google" in c.lower():  # If you say "open google"
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):  # Example: "play despacito"
        song = c.lower().split(" ")[1]    # Gets the second word (the song name)
        link = musicLibrary.music[song]   # Finds the link from your music library
        webbrowser.open(link)             # Opens that link in the browser to play

    elif "news" in c.lower():  # If you say "news", it reads the top headlines
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])  # Speaks the news headline

    else:
        output = aiProcess(c)   # For any other command → sends it to OpenAI (ChatGPT)
        speak(output)           # Speaks out the response

# This is where your main program starts
if __name__ == "__main__":
    speak("Jarvis is Starting....")

    while True:  # Keeps running → always listening for the wake word “Jarvis”

        print("recognizing...")

        try:
            with sr.Microphone() as source:   # Start using your microphone
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)  # Converts your speech to text

            if word.lower() == "jarvis":      # If you say “Jarvis”
                speak("Yes")                  # Jarvis replies “Yes”

                with sr.Microphone() as source:  # Listen again → this time for your full command
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)     # Send the command to be processed

        except Exception as e:  # If something goes wrong (like not understanding), print the error
            print("Error; {0}".format(e))


'''📝 Summary of Main Points 
Part	                                    What It Does
speak()	                    Makes Jarvis speak out loud using gTTS + pygame
aiProcess()	                Sends commands to ChatGPT and gets a reply
processCommand()	        Opens Google, Facebook, plays music, reads news, or asks ChatGPT
while True:	                Keeps listening for you to say “Jarvis”
"Jarvis Active..."	        After you say “Jarvis”, it listens to your command
except	                    Handles errors if speech is not clear
'''
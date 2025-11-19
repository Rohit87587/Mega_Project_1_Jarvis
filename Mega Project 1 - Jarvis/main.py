import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
from google import genai
import pygame
from dotenv import load_dotenv
import os

load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=GENAI_API_KEY)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function using gTTS and pygame

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# AI Processing function using Google Gemini API

def aiProcess(command):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  
            contents=f"User said: {command}. Reply as Jarvis:"
        )

        # return only text
        return response.text

    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I am unable to process that."
        

def processCommand(c):

    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        try:
            song = c.split(" ")[1]
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("Song not found.")
        except:
            speak("Please say the song name properly.")

    elif "news" in c:
        try:
            url = f"https://gnews.io/api/v4/top-headlines?lang=en&country=in&apikey={NEWS_API_KEY}"
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])

                if not articles:
                    speak("No news found.")
                else:
                    for article in articles[:5]:
                        speak(article["title"])
            else:
                speak("Unable to fetch news right now.")

        except Exception as e:
            print(e)
            speak("Error fetching news.")

    else:
        output = aiProcess(c)
        speak(output)

# Main loop to listen for wake word and process commands

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            word = recognizer.recognize_google(audio).lower()

            if word == "jarvis":
                speak("Yes?")
                print("Jarvis activated...")

                with sr.Microphone() as source:
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except Exception as e:
            print("Error:", e)




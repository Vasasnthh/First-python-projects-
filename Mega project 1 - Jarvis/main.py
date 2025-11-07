import speech_recognition as sr
import requests
import webbrowser
import time
import musicLibrary  # Make sure this file exists in the same folder
from gtts import gTTS
from groq import Groq
import pygame
import os
import random

recognizer = sr.Recognizer()
newsapi = "7ec0fd316676434592a5eb90fbfd0e60"


def aiProcess(command):
    client = Groq(api_key="")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": "give short responses"},
            {"role": "user", "content": command},
        ],
    )

    return response.choices[0].message.content


def processCommand(c):
    c = c.lower().strip()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open discord" in c:
        webbrowser.open("https://discord.com")

    elif "open github" in c:
        webbrowser.open("https://github.com")

    elif "open aws" in c:
        webbrowser.open("https://aws.amazon.com")

    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data = r.json()
        if data["status"] == "ok":
            speak("Here are the top headlines for today.")
            for article in data["articles"][:5]:
                title = article["title"]
                print(title)
                speak(title)

    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry sir, I don't have {song} in my music library.")

    else:
        output = aiProcess(c)
        speak(output)


def speak(text):
    """Convert text to speech and play using pygame safely."""
    print(f"Jarvis: {text}")

    # create unique filename
    temp_file = f"jarvis_{random.randint(1000, 9999)}.mp3"

    try:
        # make mp3
        tts = gTTS(text)
        tts.save(temp_file)

        # play it
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()

        # wait till done
        while pygame.mixer.music.get_busy():
            time.sleep(0.2)

        # stop and quit mixer (this releases file handle)
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # now delete file safely
        for _ in range(3):  # retry 3 times if Windows locks it
            try:
                os.remove(temp_file)
                break
            except PermissionError:
                time.sleep(0.3)

    except Exception as e:
        print(f"[ERROR in speak()] {e}")



if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")

            if "jarvis" in command.lower():
                time.sleep(0.5)
                speak("Yes sir")

                with sr.Microphone() as source:
                    print("Activating Jarvis...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                new_command = recognizer.recognize_google(audio)
                print(f"Command received: {new_command}")
                processCommand(new_command)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except KeyboardInterrupt:
            speak("Goodbye sir")
            break

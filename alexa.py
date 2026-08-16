
import datetime
import os
import random
import re
import subprocess
import webbrowser
 
import pyttsx3
import speech_recognition as sr
import wikipedia
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
 
FOUNDER_NAME = "Siddhant Sengar"
MUSIC_DIR = r"C:\Users\siddhant\Music"
 
 
def speak(audio: str) -> None:
    engine.say(audio)
    engine.runAndWait()
 
 
def wish_me() -> None:
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
 
    speak("I am Jarvis, sir. Please tell me how I can help you.")
 
 
def take_command() -> str:
    """Listen on the microphone and return recognized speech as lowercase text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        speak("Say that again please...")
        return "none"
 
    return query.lower()
 
 
def show_saved_wifi_passwords() -> None:
    """
    Reads Wi-Fi profiles already saved on this Windows machine using the
    built-in `netsh wlan show profile` command, and prints/speaks the ones
    that have a stored password. Only works for networks this PC has
    connected to before -- it does not attack or crack other networks.
    """
    result = subprocess.run(
        ["netsh", "wlan", "show", "profile"], capture_output=True
    ).stdout.decode(errors="ignore")
 
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", result)
 
    wifi_list = []
    for name in profiles:
        name = name.strip()
        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name],
            capture_output=True,
        ).stdout.decode(errors="ignore")
 
        if re.search(r"Security key\s*:\s*Absent", profile_info):
            continue
 
        profile_info_pass = subprocess.run(
            ["netsh", "wlan", "show", "profile", name, "key=clear"],
            capture_output=True,
        ).stdout.decode(errors="ignore")
 
        password_match = re.search(r"Key Content\s*:\s*(.*)", profile_info_pass)
        password = password_match.group(1).strip() if password_match else None
 
        wifi_list.append({"ssid": name, "password": password})
 
    if not wifi_list:
        speak("I could not find any saved Wi-Fi profiles with a stored password.")
        return
 
    speak("Reading saved Wi-Fi profiles now.")
    for i, entry in enumerate(wifi_list, start=1):
        print(i, entry)
 
    speak(f"Found {len(wifi_list)} saved Wi-Fi networks with stored passwords.")
 
 
def play_music() -> None:
    if not os.path.isdir(MUSIC_DIR):
        speak("I could not find your music folder.")
        return
 
    songs = [f for f in os.listdir(MUSIC_DIR) if os.path.isfile(os.path.join(MUSIC_DIR, f))]
    if not songs:
        speak("Your music folder is empty.")
        return
 
    song = random.choice(songs)
    os.startfile(os.path.join(MUSIC_DIR, song))
    speak(f"Playing {song}")
 
 
def say_goodbye_and_exit() -> None:
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Thanks for coming. Have a nice day.")
    elif 12 <= hour < 19:
        speak("Thanks for coming. Have a nice evening.")
    else:
        speak("Thanks for coming. Have a good night.")
    raise SystemExit
 
 
def main() -> None:
    wish_me()
    while True:
        query = take_command()
 
        if query == "none":
            continue
 
        if 'wikipedia' in query:
            search_term = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(search_term, sentences=1, auto_suggest=False)
                speak("According to Wikipedia...")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I could not find that on Wikipedia.")
 
        elif 'exit' in query:
            say_goodbye_and_exit()
 
        elif 'who is your founder' in query:
            message = f"{FOUNDER_NAME} is my founder."
            speak(message)
            print(message)
 
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
 
        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")
 
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")
 
        elif 'play music' in query:
            play_music()
 
        elif 'wifi passwords' in query or 'wi-fi passwords' in query:
            show_saved_wifi_passwords()
 
        elif 'gu kha lijiye' in query:
            speak("tu kha le")
 
        else:
            speak("Sorry, I did not understand that command.")
 
 
if __name__ == "__main__":
    main()
 

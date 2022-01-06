from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
from time import sleep
import re
import subprocess
import webbrowser
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


##
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#   speak funtion end  #


##
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good Morning ")
    elif hour>=12 and hour<18:
        speak("good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis Sir. Please tell how may I help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
      
    except Exception as e:
        #print(e)

        print("Say that again please... ")
        speak("Say that again please... ")

        return "None"
    
    return query
def hacking():
    command = subprocess.run(["netsh","wlan","show","profile"], capture_output= True).stdout.decode()
    profile = (re.findall("All User Profile     : (.*)\r", command))
    wifi_list = list()
    if len(profile)!=0:
        for name in profile:
            wifi_profile = dict()
            profile_info = subprocess.run(["netsh","wlan" , "show" , "profile" , name] , capture_output= True).stdout.decode()
            if re.search("Security key             : Absent" , profile_info):
                continue
            else:
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.run(["netsh","wlan" , "show" , "profile" , name,"key=clear"] , capture_output= True).stdout.decode()
                password = re.search("Key Content            :(.*)\r",profile_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)
   # def sid():
        speak("Starting wifi Attack")
        speak("please wait, hacking is in process.")
        print("wait...")
        sleep(2)
        print()
        #n = int(input("IF you won't to print them press 2 :- "))
        print()
        print()
        print()
        print() 
        n=0
        for x in range(len(wifi_list)):
            n = x+n
            sleep(1.24555)
            print(x+1,wifi_list[x] )
        speak("Hacking attack successfully done,. And 7 Wifi are found ")


    #sid()


    #####...............................starts here.................................####
    ##### ........................List the user input...............................#####

def tokri():
    print("sid")


 


wishMe()
while True:

    query = takeCommand().lower()
   # zspeak(" here is pagal ")

   # logic for executing tasks based on query

    if 'wikipedia' in query:



        speak('according to Wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=1)
        speak("According to wikipedia....")
        print(results)
        speak(results)
    elif 'exit' in query:
        hour = int(datetime.datetime.now().hour)
        if hour >=0 and hour<12:
                speak("Thanks , for coming. Have A nice day, Bro ")
        elif hour>=12 and hour<19:
                speak("goThanks , for coming. Have a nice evening,sid ")
        else:

                speak("Thanks , for coming. Have a good night sid ")
                exit()
    elif 'who is your founder' in query:

        speak("Mister Siddhant Sengar is my founder. And he also known sid ")
        print("Mister Siddhant Sengar is my founder. And he also known sid ")
    elif 'open youtube' in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")
            

    elif 'open stack overflow' in query:
            speak
            webbrowser.open("stackoverflow.com")
    elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
    elif 'play music' in query:
            music_dir = 'C:\\Users\\siddhant\\Music'
            song = os.listdir(music_dir)
            n = len(song)
            h = int(n/2)
            m = random.randint(0,h)
            print(song)
            os.startfile(os.path.join(music_dir, song[m]))
    elif 'wi-fi attack' in query:
            hacking()
    elif 'gu kha lijiye' in query:
            speak("tu kha le")


        #elif 'note that' in query:

        

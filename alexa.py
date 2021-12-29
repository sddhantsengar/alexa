import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


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
        return "None"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
   # zspeak(" here is pagal ")

   # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            print(results)
            speak(results)
        elif 'exit' in query:
            speak("Thanks , for coming.  Have A nice day ")
            exit()

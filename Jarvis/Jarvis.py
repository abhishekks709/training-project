import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# ---------------------offline speaking text----------------------------------------
engine = pyttsx3.init('sapi5')                   # initialisation
voices = engine.getProperty('voices')            # get voices
# print(voices[0].id)                            # voice id to change voice
engine.setProperty('voice',voices[0].id)          # set voice or change the voice


def speak(audio):
    """speak function using pyttsx3"""

    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """ Take microphone input from user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language ='en')  #Using google for voice recognition.
        print(f"User said: {query}\n")              #User query will be printed.
 
    except Exception as e:
        # print(e)
        print('say that again please...')
        return "None"
    return query


def wishMe():
    """ WishMe function has functionality to wish morning , evening and night"""

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour <= 18:
        speak('Good Afernoon!')
    else:
        speak('Good Evening!')
    speak("I am Jarvis Sir. Please tell me how may i help you")

def sendEmail(to, contant):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email id','account password')
    server.sendmail('email id', to , contant)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\Mobile\\Favourites'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in  query:
            startTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The Time is {startTime}" )

        elif 'open code' in query:
            codepath ='C:\\Users\\AKS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif 'email to abhi' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = 'abhishekrockstar.ptk@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry, I am unable to sent email')

        elif 'bye' in query:
            exit()
            





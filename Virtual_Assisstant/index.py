import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import numpy as np
import subprocess
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour <18:
        speak("Good After noon!")
    else:
        speak("good evening!")
    speak("I am ASSISTANT. Please tell me how may i help you")
def takecommand():
    '''
    it takes microphone input from user and returns string output
    '''
    r= sr.Recognizer()#object of recognition class it will help to recognize audio
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1 # so that if i take some pause between my words it does not complete the sentence
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')# converting the audio into string
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query # this function is taking the audio and returning it as a string

def sendEmail(to, content):
        f= open("D:\python\jarvis\password.txt","r")
        p=f.read()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('sushmitamukherjee2004@gmail.com', p)
        server.sendmail('sushmitamukherjee2004@gmail.com', to, content)
        server.close()
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(':','-') + '-note.txt'
    with open(file_name, 'w') as f:
        f.write(text)
    subprocess.Popen(['notepad.exe',file_name])








        




from Virtual_Assisstant.index import *
import wikipedia
import webbrowser
import os
import numpy as np

if __name__ == "__main__":
    mail = {'sushmita': 'mukherjeesushmita119@gmail.com', 'shrestha': 'paulshresthaa2209@gmail.com'}

    wishme()
    while True:
        query = takecommand().lower()  # install wikipedia also
        # logic for executing tasks based on query
        if "bye" in query:
            speak("Okay bye!!")
            break
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)  # it will show upto 2 sentence
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)  # listdir will make a list of all song in that directory
            print(songs)
            os.startfile(os.path.join(music_dir, songs[np.random.randint(0, 5)]))  # it will start the file
        elif 'the time' in query:
            hour = datetime.datetime.now().hour
            min = datetime.datetime.now().minute
            if hour >= 0 and hour < 12:
                mode = 'AM'
                if hour == 0:
                    stime = 12
                else:
                    stime = hour
            else:
                mode = 'PM'
                if hour == 12:
                    stime = 12
                else:
                    stime = hour - 12

            # strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {stime} {min} {mode}')
        elif 'open visual code' in query:
            codepath = "C:\\Users\\mukhe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open python ide' in query:
            codepath = "C:\\Users\\mukhe\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\idlelib\\idle.pyw"
            os.startfile(codepath)
        elif 'email' in query:
            try:

                speak("what should i say?")
                content = takecommand()
                print(content)
                if 'sushmita' in query:
                    to = mail['sushmita']
                elif 'shrestha' in query:
                    to = mail['shrestha']

                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif 'make a note' in query:
            speak('What should i write?')
            content = takecommand()
            if 'None' not in content:
                speak('Okay, I am making a note')
                note(content)
                speak(" I have made a note")
            else:
                speak("note has not been made")
        elif 'check mail' in query:

            speak('opening gmail')

            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox")

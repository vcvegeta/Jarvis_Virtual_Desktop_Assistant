import pyttsx3                          # text (string) to speech recognition external module
import datetime
import speech_recognition as sr              # eternla module , so install it first  
import pyaudio                           #  PyAudio is an external module in Python , its the bridge between Python and your computer’s microphone/speaker hardware. It helps Python: Access the microphone, Record audio in real-time, Play audio.  
                                        # When you use: with sr.Microphone() as source: Behind the scenes, it uses pyaudio to: Connect to the physical microphone and stream your voice into Python.
import wikipedia
import webbrowser
import os
import smtplib


engine= pyttsx3.init("sapi5")           # initialzing the t2s engine using microsoft's built in sapi5 API which is a speech api
# print(engine)                           # returns engine object  ie <pyttsx3.engine.Engine object at 0x000001ADD299FA10>

voices= engine.getProperty("voices")             # "voices" is the name of a property you're asking the engine to give you, It tells the engine “Give me the list of all available voices.”
# print(voices)                                    # returns 2 voice object inside a LIST ie [ <pyttsx3.voice.Voice object at 0x0000022212A6C2F0>, <pyttsx3.voice.Voice object at 0x0000022212718E10> ]
# print(voices[0].id)                               # returns the voice of a boy David at 0th index and returns a girl Zira at index 1
engine.setProperty("voice",voices[0].id)          # We have chosen the vouce that we need to run our engine
engine.setProperty('rate', 270)                    # Increase the number for faster speaking pace 


def speak(audio):                        # takes string input
    engine.say(audio)                   # Queues the text to be spoken, does not speak immediately , more like: adding a message to the speaker's to-do list
    engine.runAndWait()                 # Starts the speech engine, This is when the speech happens, Speak everything in the queue, and don’t move to the next line of code until all the speaking is finished.
    
def wishMe():                                             # Wishes the user based on current time ie GM, GA and GE    
    current_hour= int(datetime.datetime.now().hour)      # finds out current hour and convert that to integer and then store it. 
    # print(current_hour) 
    if (current_hour>=0 and current_hour<12):              # Wishes the user as per the current hour.
        speak("Good Morning!") 
    elif(current_hour>=12 and current_hour<=18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Your AI desktop assistant. Please tell me how may I help you today")

def takeCommand():        # takes microphone input (speech) from the user and then converts it to a text automatically
    r= sr.Recognizer()      # Recognizer() is a class here which when gets invoked () means object gets created and then the constructor is automatically executed as well , name of object here is r which can be used to access the attributes and methods of class Recognizer()

    with sr.Microphone() as source:     # .Microphone() hears your voice from the microphone whereas .Recognizer() understands what you said and (converts speech to text).          source= sr.Microphone() is the object name here.
                                        #  This is where the microphone is activated (opened) and ready to listen.  Source is now your live mic. 
        print("Listening........")      # .Microphone() sirf capture krega audio but .Recognizer() is the one that controls how listening works. Usko btaega ki kb start krna hai , kitna rukna h aur user agar 2 second chup rhe toh means ki usne apna input de dia hai or how to handle silence ,etc
        r.pause_threshold=2          # seconds of non-speaking audio  before a phrase is considered complete. If you stop speaking for 2 seconds, the recognizer will think you’ve finished your sentence and will finalize the input.
        audio= r.listen(source)      # means Recognizer r, please listen to the sound coming from the microphone source.  The Recognizer object (r) starts recording audio from the microphone (source).  It listens until: It hears silence (based on pause_threshold). Then, It stores the raw audio data in the variable audio,But it has not interpreted (converted to text) yet.
        #       Why doesn’t Microphone() have .listen()?
        #       The Microphone object (source) only provides raw audio — it’s like your ears.
        #       The Recognizer object (r) is the brain — it knows how to: detect when someone starts and stops talking, handle silence, convert it into usable audio data
        #       You're listening from the mic, but you're using the Recognizer's .listen() method to do it properly
        
        try:
            print("Recognizing........")
            user_said=r.recognize_google(audio, language="en-in")           # Converts recorded speech to text(string)
            print(f"User said: {user_said}\n")                              # query ko likhdia hai user_said
        except Exception as e:
            # print(e)  # captures the error
            print("Say that again please!!")
            return "None" 
        return user_said                                         # each function should return a value and try me pass hone k bad return krega takeCommand() function ko user_said variable which has text interpreted by the speech recorded.


def sendEmail(to, content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()                                    # .ehlo() is a method that sends an EHLO command to the mail server, which stands for: Extended hello!  It introduces your client to the SMTP server.
    server.starttls()
    server.login("vc636sml@gmail.com","your_password_here")                # enter your password code here             
    server.sendmail("vc636sml@gmail.com", to, content)          # sendmail takes from,to,content as the arguments  
    server.close() 


               
if __name__=="__main__":                # entry point of program execution
    speak("Hi Viraat. How are you?")        
    wishMe()

    while True:           # infinite loop chalta rhega and jarvis will keep asking us questions infinitely 
        # takeCommand()
        user_said=takeCommand().lower() 

        # Logic for executing the tasks based on what 'user said' 
        if "wikipedia" in user_said:
            speak("Searching Wikipedia..... , Please wait! ")
            user_said=user_said.replace("Wikipedia", "")       # means if I entered SRK Wikipedia , wikipedia will be replaced with "" and we will be searching just SRK now.
            results= wikipedia.summary(user_said, sentences=2)
            print(results)
            speak(results) 
        elif( "open youtube" in user_said):
            webbrowser.open("youtube.com") 
        elif("open google" in user_said):
            webbrowser.open("google.com")
        elif("open stack overflow" in user_said):
            webbrowser.open("stackoverflow.com")
        elif("open google" in user_said):
            webbrowser.open("google.com")
        elif("play music" in user_said):
            music_dir=r"C:\Users\subod\Downloads\Music"
            music=os.listdir(music_dir)
            # print(music)
            os.startfile(os.path.join(music_dir,music[0]))
        elif("time" in user_said):
            strTime=datetime.datetime.now().strftime("%H-%M-%S")
            print(strTime)
            speak(f"Sir, the time is: {strTime}") 
        elif ("open code" in user_said):
            vsCodePath="C:\\Users\\subod\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    # double \\ to remove escape sequence characters and treat it as the path as it is
            os.startfile(vsCodePath)
        elif ("send email" in user_said):
            try:
                print("What should I say?")
                content= takeCommand()              # returns user_said value
                to="vc636sml@gmail.com"  
                sendEmail(to,content)
                print("Email sent")     
                speak("Sir, The Email has been sent")
            except Exception as e:
                print(e) 
                speak("Sorry Sir, this email can't be send right now!")
        elif("jarvis quit" in user_said):
            speak("Quitting now. See you later! ")      
            quit()        









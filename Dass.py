import os,sys
import requests
import win32com.client  #library for voice interface
import speech_recognition as sr
import time
from datetime import datetime
from tkinter import *   #tkinter GUI Module
from pprint import pprint
from firebase import firebase


#Main:
root=Tk()
root.title("Daas")
root.configure(background="black")
#canvas = Canvas(width=850, height=450, bg='black')
#canvas.pack()

#==================startin setup=====================================================

#frame akgrownd
#photo = PhotoImage(file='C:\\Users\\Vishal Watts\\Desktop\\DassAI\\Watts.png')
#canvas.create_image(0,0, image=photo, anchor=NW)
#Label(root,image=photo,bg="black",).grid(row=0,column=0, sticky=W)
#Label(root,text="mr.watts",bg="yellow",fg="black",font="none 12 bold").grid(row=0,column=0,sticky=W)
#dass wishing you
now=datetime.now()
hour=now.hour
minute=now.minute

wnote=0

if hour < 12:
    if hour > 4:
        wnote= "good morning"
        #print("good morning")
if hour > 12:
    if hour < 16:
        wnote= "good aftrnoon"
        #print("good afternoon")
if hour > 16:
    if hour < 20:
        wnote= "good evening"
        #print("good evining")
if hour > 20:
    if hour < 23:
        if minute < 59:
            wnote= "Glad to see you again"
            #print("Glad to see you again")
if hour == 0:
    if minute > 1:
        wnote= "Glad to see you again"
        #print("Glad to see you again")
if hour > 0:
    if hour < 4:
        wnote= "Glad to see you again"
        #print("Glad to see you again")



#=========fun==============

#time
def trick():
    time_string=time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,trick)

#==============================Weather=====================
citydb=StringVar()
tempdb=StringVar()
humiditydb=StringVar()
pressuredb=StringVar()
winddb=StringVar()
descriptiondb=StringVar()
url = "http://api.openweathermap.org/data/2.5/weather?"
geocoordinate = "lat=30.6050&lon=74.2558&units=metric"
#geocoordinate = "lat=30.6050&lon=74.2558&units=metric"
api = "&appid=5d57bc593b5943d740e2f4e5f6c82411"
res = requests.get(url + geocoordinate + api)
data = res.json()
#Ver
city=("City Name   : {}".format(data['name']))
temp=("Tempature   : {} C".format(data['main']['temp']))
humidity=("Humidity    : {} %".format(data['main']['humidity']))
pressure=("Pressure    : {}".format(data['main']['pressure']))
wind=("Wind Speed  : {} mph".format(data['wind']['speed']))
description=("Description : {}".format(data['weather'][0]['description']))
#print(city)
# label
liib1=Label(root,font=("times",16,"bold"),textvariable=citydb,fg="white",bg="black")
liib2=Label(root, font=("times",16,"bold"),textvariable=tempdb,fg="white",bg="black")
liib3=Label(root, font=("times",16,"bold"),textvariable=humiditydb,fg="white",bg="black")
liib4=Label(root, font=("times",16,"bold"),textvariable=pressuredb,fg="white",bg="black")
liib5=Label(root, font=("times",16,"bold"),textvariable=winddb,fg="white",bg="black")
liib6=Label(root, font=("times",16,"bold"),textvariable=descriptiondb,fg="white",bg="black")

liib1.pack()
liib2.pack()
liib3.pack()
liib4.pack()
liib5.pack()
liib6.pack()

citydb.set(city)
tempdb.set(temp)
humiditydb.set(humidity)
pressuredb.set(pressure)
winddb.set(wind)
descriptiondb.set(description)

clock=Label(root,font=("times",50,"bold"),bg="black",fg="white")
clock.pack(side=TOP, fill=X)
trick()
owner = Label(root, text="Powerd by Mr. Watts", anchor=W, relief=SUNKEN, bd=1)
owner.pack(side=BOTTOM, fill=X)
#systime=time.strftime("%H:%M:%S")

#welcom voice note
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(wnote)
speaker.Speak("mister vishal wattss The current time is")
speaker.Speak(time.strftime("%H:%M:%S"))
speaker.Speak(str("weather is")+temp+humidity+wind+description)


#=====================================serial=====================================
#firebase = firebase.FirebaseApplication('https://applications-29c71.firebaseio.com/', None)
#while True:
    #Fan=firebase.get('/Home_Automation', 'Fan')
    #Bulb=firebase.get('/Home_Automation', 'Bulb')
#=====================================AI=========================================
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        speaker.Speak("sorry i can't understand")
        #print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'hello' in command:
        speaker.Speak("hi")

    if 'hi' in command:
        speaker.Speak("hello")
        
    elif 'how are you' in command:
        speaker.Speak("i'm fine you say")

    elif 'what\'qs going on' in command:
        speaker.Speak('Just doing my thing')
        
    elif 'i am fine' in command:
        speaker.Speak("greate")

    elif 'weather' in command:
        speaker.Speak("the weather is")

    elif 'awesome' in command:
        speaker.Speak("thats greate")

    elif 'computer' in command:
        speaker.Speak("yes sir")

    elif 'what time is it' in command:
        speaker.Speak(time.strftime("%H:%M:%S"))

#loop to continue executing multiple commands
while True:
    assistant(myCommand())

#====================================End=========================================
root.mainloop

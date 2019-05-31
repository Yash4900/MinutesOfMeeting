import speech_recognition as sr 
from os import path
from pprint import pprint


def recognizerWithMicrophone():

    r=sr.Recognizer()#creating instance of recognizer class

    #using microphone for source input
    with sr.Microphone() as source:
        print("Speak!")
        audio = r.listen(source) #collecting the audio for recognizer
        print("Over")

    #translate..

    try:
        text = r.recognize_google(audio) #the text stores whatever google api returns 
        print("you said,",text) #printing what google api returned

    except:
        print("Could not recognize")
        #exception if google api doesn't understand what you said


def recognizerWithAudioFile():
    audio_file=path.join(path.dirname(path.realpath(__file__)),"sample.wav")
    r=sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio=r.record(source)

    try:
        output=r.recognize_google(audio,show_all=True)#show all = true will show all possibilites of how google translates this audio to text
        print("Over")
        pprint(output)
        #output also shows the accuracy of its conversion...check key confidence and transcript in output means the difference conversions of the audio file
        
    except:
        print("Could not recognize")#exception if google api doesn't understand 


choice=int(input("Enter a choice 1)Microphone 2)Audio File"))
if choice==1:
    recognizerWithMicrophone()
else:
    recognizerWithAudioFile()





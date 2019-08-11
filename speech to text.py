# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import speech_recognition as sr
AUDIO_FILE=("rec.wav")
r=sr.Recognizer()#initialize the recognizer
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source);#read the audio file
try:
    print("audio file contains " +r.recognize_google(audio))
except sr.UnknownValueError:
    print("can't understand")
except sr.RequestError:
    print("could not get results")
    
    
    
    


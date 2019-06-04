import pyttsx3
import matplotlib.pyplot as plt
import mfcc

absCorr = mfcc.correlation('shivam.wav', 'google.wav')

print(absCorr)

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female

correlationThreshold = 100  # if the value of correlation is higher than this threshold, the audio samples are sufficiently similar

if absCorr <= correlationThreshold:
    engine.say("Authentication successful")
    engine.runAndWait()

if absCorr >= correlationThreshold:
    engine.say("Authentication failed")
    engine.runAndWait()





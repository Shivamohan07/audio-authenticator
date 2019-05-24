import pyttsx3
import fourier


fourierA, lengthA = fourier.fourier('output.wav')
fourierB, lengthB = fourier.fourier('output1.wav')

absCorr = fourier.correlation(fourierA, fourierB)

print(absCorr)

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female

correlationThreshold = 50000  # Random threshold

if absCorr >= correlationThreshold:
    engine.say("Authentication successful")
    engine.runAndWait()

if absCorr <= correlationThreshold:
    engine.say("Authentication failed")
    engine.runAndWait()

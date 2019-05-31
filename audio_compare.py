import pyttsx3
import fourier
import matplotlib.pyplot as plt

fourierA, lengthA = fourier.fourier('test.wav')
fourierB, lengthB = fourier.fourier('test3.wav')

absCorr = fourier.correlation(fourierA, fourierB)

print(absCorr)

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female

correlationThreshold = 100000  # if the value of correlation is higher than this threshold, the audio samples are sufficiently similar

if absCorr >= correlationThreshold:
    engine.say("Authentication successful")
    engine.runAndWait()

if absCorr <= correlationThreshold:
    engine.say("Authentication failed")
    engine.runAndWait()


plt.plot(abs(fourierA[:(1024-1)]),'r')
plt.show()

plt.plot(abs(fourierB[:(1024-1)]),'r')
plt.show()





import pyaudio
import wave
import speech_recognition as sr
import pyttsx3



engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female
r = sr.Recognizer()

with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    engine.say("Please speak login to login to the system, or register to register yourself")
    engine.runAndWait()
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=4)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
    except:
        engine.say("Sorry could not understand, please speak again")
        engine.runAndWait()


if text == "login":
    engine.say("Please speak authorization passcode")
    engine.runAndWait()
elif text == "register":
    engine.say("You choose registration, Please speak your passcode after 2 seconds ")
    engine.runAndWait()
else:
    engine.say("You spoke " + text + " This option is not supported")
    engine.runAndWait()
    exit(0)



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 1000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "google.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording : STARTED")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #print(" ")
    data = stream.read(CHUNK)
    #print(data)
    frames.append(data)
    print(". ")

print("Recording : COMPLETED")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

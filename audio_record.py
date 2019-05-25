
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 1000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output2.wav"

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

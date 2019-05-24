# Audio Authenticator
This is a sample python project for building voice authentication system.

# Requirements

* pyaudio
* wave
* pyttsx3
* scipy
* numpy

# Usage
First record audio using 'audio_record.py'
--> This will output a 'output.wav' file -- Consider as base file

Again record audio using 'audio_record.py'
--> This time name the output as 'output1.wav' file -- Consider as test file

Then run audio_compare to check similarity 
between basefile and testfile

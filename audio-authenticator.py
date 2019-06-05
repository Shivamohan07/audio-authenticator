import speech_recognition as sr
import pyttsx3
import audio_compare
import audio_record
import time
#Initialize speaking engine

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female


def login():
    audio_record.record_audio("login.wav")
    result = audio_compare.compare("register.wav", "login.wav")
    if result:
        engine.say("Authorization successful")
        engine.runAndWait()
    else:
        engine.say("Authorization failed")
        engine.runAndWait()


def register():
    audio_record.record_audio("register.wav")


keywords = [("visa", 1), ("hey visa", 1), ]
commands = [("login", 1), ("register", 1), ]
r = sr.Recognizer()
source = sr.Microphone()


def callback(recognizer, audio):  # this is called from the background thread

    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)

        # Look for your "Ok Google" keyword in speech_as_text
        if "visa" in speech_as_text or "hey visa":
            recognize_main()

    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def recognize_main():
    print("Recognizing Main...")
    re = sr.Recognizer()
    engine.say("Welcome!! Please speak login, to login to the system, or register, to register yourself")
    engine.runAndWait()
    with sr.Microphone() as source1:
        re.energy_threshold = 4000
        audio = re.listen(source1, phrase_time_limit=3)  # listen to the source
        text = re.recognize_google(audio)
        print("listened")
        try:
            text = re.recognize_google(audio)
            print(text)
        except Exception as e:
            print(e)
            engine.say("Sorry could not understand, please speak again")
            engine.runAndWait()

    if text == "login":
        engine.say("Please speak authorization passcode")
        engine.runAndWait()
        login()
    elif text == "register":
        engine.say("You choose registration, Please speak your name after 2 seconds ")
        engine.runAndWait()
        register()
    else:
        engine.say("You spoke " + text + ", this option is not supported")
        engine.runAndWait()
        exit(0)


def start_recognizer():
    r.listen_in_background(source, callback)
    time.sleep(1000000)



#start_recognizer()
recognize_main()
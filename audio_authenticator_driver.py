import speech_recognition as sr
import pyttsx3
import time
import register
import login

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female

keywords = [("visa", 1), ("hey visa", 1), ]
commands = [("login", 1), ("register", 1), ]


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
    r = sr.Recognizer()
    engine.say("Hello, Please speak your name ")
    engine.runAndWait()
    listened = 0
    while listened != 1:
        with sr.Microphone() as source:
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                name = r.recognize_google(audio)
                print(name)
                listened = 1
            except Exception as e:
                print(e)
                engine.say("Sorry could not understand, please speak again")
                engine.runAndWait()

    re = sr.Recognizer()
    engine.say("Welcome " + name + "!! Speak login, to login, or register, to register, else speak cancel")
    engine.runAndWait()
    option = 0
    while option != 1:
        with sr.Microphone() as source1:
            try:
                re.adjust_for_ambient_noise(source1)
                audio = re.listen(source1)
                text = re.recognize_google(audio)
                print(text)
                option = 1
            except Exception as e:
                print(e)
                engine.say("Sorry could not understand, please speak again")
                engine.runAndWait()

    if text == "login":
        engine.say("Please speak authorization passcode")
        engine.runAndWait()
        result = login.login(name)
        if result == 'true':
            engine.say("Authentication Successful !!!")
            engine.runAndWait()
        else:
            engine.say("Authentication Failed !!!")
            engine.runAndWait()
    elif text == "register":
        engine.say("You chose registration")
        engine.runAndWait()
        register.register(name)
    elif text == "cancel":
        engine.say("You chose cancel, Bye!!!")
        engine.runAndWait()
        exit(0)
    else:
        engine.say("You spoke " + text + ", this option is not supported")
        engine.runAndWait()
        exit(0)


def start_recognizer():
    rM = sr.Recognizer()
    sourceM = sr.Microphone()
    rM.listen_in_background(sourceM, callback)
    time.sleep(1000000)


#start_recognizer()
recognize_main()

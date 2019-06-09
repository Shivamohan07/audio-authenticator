import pyttsx3
import audio_record
import audio_auth_train
import os

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female


def register(name):

    engine.say("Please set your passcode by speaking it 5 times")
    engine.runAndWait()
    if not os.path.exists("training_data_input/" +name):
        os.makedirs("training_data_input/" +name)

    for count in range(5):
        engine.say("Sample " + str(count) + " : Speak Now ")
        engine.runAndWait()
        audio_record.record_audio("training_data_input/" +name + "/" + name + "-" + str(count) + ".wav")
    engine.say("Registration successful, Thank you ")
    engine.runAndWait()
    audio_auth_train.train(name)




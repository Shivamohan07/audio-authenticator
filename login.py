import os
from sklearn import preprocessing
import python_speech_features as mfcc
import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
import warnings
warnings.filterwarnings("ignore")
import pyttsx3
import audio_record

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Lower -> Slower
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 - Male, 1 - Female


def calculate_delta(array):
    """Calculate and returns the delta of given feature vector matrix"""

    rows, cols = array.shape
    deltas = np.zeros((rows, 20))
    N = 2
    for i in range(rows):
        index = []
        j = 1
        while j <= N:
            if i - j < 0:
                first = 0
            else:
                first = i - j
            if i + j > rows - 1:
                second = rows - 1
            else:
                second = i + j
            index.append((second, first))
            j += 1
        deltas[i] = (array[index[0][0]] - array[index[0][1]] + (2 * (array[index[1][0]] - array[index[1][1]]))) / 10
    return deltas


def extract_features(audio, rate):
    """extract 20 dim mfcc features from an audio, performs CMS and combines
    delta to make it 40 dim feature vector"""

    mfcc_feat = mfcc.mfcc(audio, rate, 0.025, 0.01, 20, appendEnergy=True)

    mfcc_feat = preprocessing.scale(mfcc_feat)
    delta = calculate_delta(mfcc_feat)
    combined = np.hstack((mfcc_feat, delta))
    return combined


def login(name):
    engine.say("Speak your passcode : Now ")
    engine.runAndWait()
    audio_record.record_audio("test_data_input\\" + name + ".wav")
    modelpath = "training_result\\"

    gmm_files = [os.path.join(modelpath, fname) for fname in
             os.listdir(modelpath) if fname.endswith('.gmm')]

    models = [cPickle.load(open(fname, 'rb')) for fname in gmm_files]
    speakers = [fname.split("\\")[-1].split(".gmm")[0] for fname
            in gmm_files]
    print(speakers)
    sr, audio = read("test_data_input\\" + name + ".wav")
    vector = extract_features(audio, sr)
    log_likelihood = np.zeros(len(models))
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
    winner = np.argmax(log_likelihood)
    print("\tdetected as - ", speakers[winner])
    if name== speakers[winner]:
        return 'true'
    else :
        return 'false'


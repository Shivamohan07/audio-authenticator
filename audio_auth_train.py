import numpy as np
from sklearn import preprocessing
import python_speech_features as mfcc
import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture as GMM
import warnings
warnings.filterwarnings("ignore")


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


def train(name):
    source = "training_data_input/"
    # path where training speakers will be saved
    dest = "training_result/"
    train_file = "development_set_enroll"
    file_paths = open(train_file, 'r')
    count = 1
    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())
    for i in range(5):
        # read the audio
        sr, audio = read("training_data_input/" +name + "/" + name + "-" + str(i) + ".wav")
        vector = extract_features(audio, sr)
        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))
        if count == 5:
            gmm = GMM(n_components=16, max_iter=200, covariance_type='diag', n_init=3)
            gmm.fit(features)
            # dumping the trained gaussian model
            picklefile = name + ".gmm"
            print(picklefile)
            cPickle.dump(gmm, open(dest + picklefile, 'wb'))
            print('+ modeling completed for speaker:', picklefile, " with data point = ", features.shape)
            features = np.asarray(())
            count = 0
        count = count + 1
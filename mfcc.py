import librosa
import matplotlib.pyplot as plt
from dtw import dtw
from numpy.linalg import norm
import librosa.display


def correlation(f1, f2):
    y1, sr1 = librosa.load(f1)
    y2, sr2 = librosa.load(f2)
    mfcc1 = librosa.feature.mfcc(y1, sr1)
    librosa.display.specshow(mfcc1)
    mfcc2 = librosa.feature.mfcc(y2, sr2)
    dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1)) # Lower the dist similar the audio : 0 for same audios
    plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
    plt.plot(path[0], path[1], 'w')   #creating plot for DTW
    #plt.show()  #To display the plots graphically
    return dist
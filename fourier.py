from scipy.io import wavfile  # get the api
from scipy.fftpack import fft, ifft
import numpy
from scipy.stats import pearsonr


def fourier(wave_file):
    fs, data = wavfile.read(wave_file)  # load the data
    track = data.T[0]
    b = [(ele / 2 ** 8.) * 2 - 1 for ele in track]  # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b)
    # Calculate length, only half length shows the real signal i.e actual signal length d//2
    d = len(c)
    return c, d


def correlation(f1, f2):
    return max(abs(ifft(f1 * numpy.conj(f2))))


def correlation_normalized(f1, f2):
    return ifft(f1 * numpy.conj(f2))/(numpy.linalg.norm(f1)*numpy.linalg.norm(f2))

def correlation_pearson(f1, f2):
    return pearsonr(f1, f2)

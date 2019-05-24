
from scipy.io import wavfile # get the api
from scipy.fftpack import fft, ifft
import numpy


def fourier(wave_file):
    fs, data = wavfile.read(wave_file)  # load the data
    a = data.T[0]  # this is a two channel soundtrack, I get the first track
    b = [(ele / 2 ** 8.) * 2 - 1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b)  # calculate fourier transform (complex numbers list)
    d = len(c)  # you only need half of the fft list (real signal symmetry)
    return c, d


def correlation(f1,f2):
    return max(abs(ifft(f1 * numpy.conj(f2))))

from scipy.io import wavfile # get the api
from scipy.fftpack import fft, ifft
import numpy


def fourier(wave_file):
    fs, data = wavfile.read(wave_file)  # load the data
    # Get Track
    track = data.T[0]

    b = [(ele / 2 ** 8.) * 2 - 1 for ele in track]  # this is 8-bit track, b is now normalized on [-1,1)

    # calculate fourier transform (complex numbers list)
    c = fft(b)

    # Calculate length, only half length shows the real signal i.e actual signal length d//2
    d = len(c)

    return c, d


def correlation(f1, f2):
    return max(abs(ifft(f1 * numpy.conj(f2))))
#def correlation(f1, f2):
#    return numpy.corrcoef(ifft(f1 * numpy.conj(f2)))

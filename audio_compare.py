import pyttsx3
import matplotlib.pyplot as plt
import mfcc


def compare(file1,file2):
    absCorr = mfcc.correlation(file1, file2)
    print(absCorr)
    correlationThreshold = 100  # if the value of correlation is higher than this threshold, the audio samples are sufficiently similar
    return absCorr <= correlationThreshold





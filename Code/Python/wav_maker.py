import numpy as np
from scipy.io.wavfile import write as wr
# from matplotlib import pyplot as plt


def sound_recovery(results, freq):
    # Given data is rescaled in order to use with the function
    min_value = min(results)
    for i in range(len(results)):
        results[i] -= min_value
    max_value = max(results)
    for i in range(len(results)):
        results[i] = (results[i] * 65535)//max_value - 32767

    data = np.int16(results)

    wr('test.wav', freq, data)

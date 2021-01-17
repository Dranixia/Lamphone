# from obspy.signal.filter import bandstop
from wav_maker import sound_recovery


def filtering(input_arr, fs=1126):
    output_arr = [x for x in input_arr]

    # ENABLE THE PART BELOW ONLY IF BULB HAS ITS' OWN NOISE
    # Filtering bulbs frequencies
    # bulb_fs = 50  # Freq of the bulb we are spying on
    # i = bulb_fs
    # while i < fs/2:
    #     output_arr = bandstop(output_arr, i, i, fs)
    #     i += bulb_fs

    # Speech enhancement - scaling to [-1, 1]
    max_f = max(output_arr)
    min_f = min(output_arr)
    for i in range(len(output_arr)):
        output_arr[i] = -1 + ((output_arr[i] - min_f)*2)/(max_f - min_f)

    # Requires a higher quality of ADC, lower part is for future realisation, testing and debugging
    # Equalizer is in the same folder
    # Equalization
    # eq_signal = [0 for _ in range(len(output_arr))]
    # for i in range(len(output_arr)):
    #     for j in range(len(equalizer)):
    #         if i - j > 0:
    #             eq_signal[i] += output_arr[i-j]*eq_signal[j]

    return output_arr


if __name__ == '__main__':
    data = []
    with open("pam_pam.txt", encoding="utf-8", errors="ignore") as f:
        for line in f.readlines():
            data.append(int(line.strip()))

    data = filtering(data, 1126)
    sound_recovery(data, 1126)

import serial
import numpy as np
import matplotlib.pyplot as plt
from time import time


def file_check(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            int(line.strip())


if __name__ == '__main__':
    ser = serial.Serial('COM3', 115200, timeout=3)
    res = []
    ser.flushInput()
    digits = 0

    start = time()
    while digits < 20000:
        try:
            ser_bytes = ser.readline()
            decoded = int(ser_bytes.decode())
            res.append(decoded)
            digits += 1
        except ValueError:
            continue
    duration = round(time() - start, 2)
    print(f'time = {time() - start}')
    ser.close()

    true_res = []
    std = max(np.std(res), 1)
    print(std)
    avg = np.mean(res)
    for el in res:
        if abs(el - avg) < 3*std:
            true_res.append(el)

    m = min(true_res)
    for i in range(len(true_res)):
        true_res[i] -= m

    step = 5/max(true_res)
    for i in range(len(true_res)):
        true_res[i] = round(step*true_res[i], 1)

    # for i in res:
    #     print(i)

    with open("readings.txt", "w", encoding="utf-8", errors="ignore") as file:
        for digit in true_res:
            file.write(str(digit) + "\n")

    plt.plot(true_res)
    plt.xlabel('num of data reads)')
    plt.ylabel('Potentiometer Reading')
    plt.title(f'Potentiometer Reading vs. number of readings for time {duration}')
    plt.show()

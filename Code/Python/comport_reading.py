import serial


if __name__ == 'main':
    ser = serial.Serial('COM5', 115200, timeout=1)
    res = []
    ser.flushInput()
    i = 0

    while i < 5000:  # How many reading you need, the Frequency is 1126
        try:
            ser_bytes = ser.readline()
            decoded = int(ser_bytes.decode())
            res.append(decoded)
            i += 1
        except ValueError:
            continue

    ser.close()

    with open("readings_song.txt", "w", encoding="utf-8", errors="ignore") as file:
        for digit in res:
            file.write(str(digit) + "\n")

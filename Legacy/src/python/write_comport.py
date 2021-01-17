import serial

ser = serial.Serial("COM4", 115200)

with open("readings.txt", "r", encoding="utf-8", errors="ignore") as file:
    for line in file.readlines():
        ser.write(int(float(line.strip())*10))

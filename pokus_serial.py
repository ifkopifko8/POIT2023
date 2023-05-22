import serial

ser = serial.Serial("/dev/ttyS0")
ser.baudrate = 9600
read_ser = ser.readline()

while True: 
	line = ser.readline()
	print(line.decode())
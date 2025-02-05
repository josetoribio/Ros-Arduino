# Importing Libraries 
import serial 
import time


# Replace 'COM3' with your Arduino's serial port
ser = serial.Serial(port='/dev/ttyACM0',baudrate=115200, timeout=.1) 
time.sleep(0.05)  # Give Arduino time to initialize
ser.write("testing".encode('utf-8'))
while True: 
	string_to_send = input("Turn On or Off the SERVO: ")
	ser.write(string_to_send.encode('utf-8'))  # Encode the string to bytes
	print(string_to_send)

ser.close()
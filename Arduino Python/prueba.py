import serial
import time

arduino = serial.Serial('COM3',9600)

while True:

	time.sleep(2)
	command = input("Ingrese el comando: ")
	arduino.write(command.encode()) #serial.Serial('COM3',9600)
	
arduino.close()

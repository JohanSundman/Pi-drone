import time
import imu # Gyro & accelerometer

def sensorLoop():

	# Create the Imu object
	sensor = imu.Imu()

	# Sensor loop
	while True:
		sensor.merge() # Update the sensor
		print("HELLO FROM SENSOR")
		time.sleep(1);

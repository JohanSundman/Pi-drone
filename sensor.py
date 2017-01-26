import threading
import time
import imu # Gyro & accelerometer

class Sensor(threading.Thread):
	def __init__(self):
		# Make sure the parent's init gets a call
		threading.Thread.__init__(self)
		
		# Create the Imu object
		self.sensor = imu.Imu()

	# Sensor loop
	def run(self):
		self.sensor.merge() # Update the sensor
		print("HELLO FROM SENSOR")
		time.sleep(1);

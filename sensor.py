import threading
import time
import imu # Gyro & accelerometer

class Sensor(threading.Thread):
	def __init__(self):
		# Make sure the parent's init gets a call
		threading.Thread.__init__(self)

		# Create the Imu object
		self.imu = imu.Imu()

	# Sensor loop
	def run(self):
		# Start the loop
		while True:
			self.imu.merge() # Update the sensor
			time.sleep(.01);

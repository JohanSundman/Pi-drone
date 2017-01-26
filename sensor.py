import threading
import time
import imu # Gyro & accelerometer

class Sensor(threading.Thread):
	def __init__(self, delay = .01):
		# Make sure the parent's init gets a call
		threading.Thread.__init__(self)

		self.delay = delay # Set the delay
		self.imu = imu.Imu() # Create the Imu object

	# Sensor loop
	def run(self):
		# Start the loop
		while True:
			self.imu.merge() # Update the sensor
			time.sleep(self.delay);

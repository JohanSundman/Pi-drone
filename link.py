# Link between the hardware and software
# Functions that communicate with the sensors

# Import the packages communicating with the hardware
import smbus # Raspberry pi i2c 
import RPi.GPIO as GPIO # Raspberry pi gpio pins


def read_byte(adress, adr):
    return bus.read_byte_data(adress, adr)

def read_word(adress, adr):
    high = bus.read_byte_data(adress, adr)
    low = bus.read_byte_data(adress, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adress, adr):
    val = read_word(adress, adr)
    if(val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def wake_up(adress, power_mgmt):
	bus.write_byte_data(adress, power_mgmt, 0) # wake it up from sleep mode

# The buss
bus = smbus.SMBus(1) # Argument might be either 0 or 1

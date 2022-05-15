import smbus
import time

#ic2 address
DEVICE = 0x23 

#light thresholds
TOO_BRIGHT = 500
BRIGHT = 100
NORMAL = 15
DARK = 5

#data registers for I2C
POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07
CONTINUOUS_LOW_RES_MODE = 0x13
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21
ONE_TIME_LOW_RES_MODE = 0x23

bus = smbus.SMBus(1)

#converts raw analogue reading into a human-readable lux measurement
def convertToNumber(data):
	result = (data[1] + (256 * data[0])) / 1.2
	return (result)
#end def

#reads data from the selected I2C device and register
def readLight(addr=DEVICE):
	data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
	number = convertToNumber(data)
	return number
#end def
	
#main program
def main():
	
	while True:
		lightLevel=readLight()
		#print("Light level : " + format(lightLevel,'.2f') + " lx")
		if (lightLevel >= TOO_BRIGHT):
			bright = "Too bright"
		elif (lightLevel >= BRIGHT):
			bright = "Bright"
		elif (lightLevel >= NORMAL):
			bright = "Normal"
		elif (lightLevel >= DARK):
			bright = "Dark"
		elif (lightLevel < DARK):
			bright = "Too dark"
		else:
			bright = "Error. Light sensor"
		
		print(bright)
			
		time.sleep(0.5)
	#end while
#end def

#runs main program
if __name__ == "__main__":
	main()
#end if

import time
import board
import busio
import RPi.GPIO as GPIO

from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# Set up I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
chan = AnalogIn(ads, ADS1115.P0)  # Use channel 0

# Set up GPIO for digital read
Digital_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Digital_PIN, GPIO.IN)

print('[Press CTRL + C to end the script!]')

try:  # Main program loop
    while True:
        analog = chan.value  # 16-bit ADC value (0–65535)
        # Or use chan.voltage for the actual voltage if you want
        digital = GPIO.input(Digital_PIN)
        print('Digital: {} - Analog: {}'.format(digital, analog))
        time.sleep(0.002)
except KeyboardInterrupt:
    print('\nScript end!')
finally:
    GPIO.cleanup()

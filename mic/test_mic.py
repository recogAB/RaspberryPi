import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ADS1115 = Adafruit_ADS1x15.ADS1115(busnum=1)
GAIN = 1
Digital_PIN = 22
GPIO.setup(Digital_PIN, GPIO.IN)
print('[Press CTRL + C to end the script!]')
try: # Main program loop
    while True:
        analog = ADS1115.read_adc(0, gain=GAIN) # ADC channel 0
        digital = GPIO.input(Digital_PIN)
        print('Digital: {} - Analog: {}'.format(digital, analog))
        time.sleep(0.002)
    # Scavenging work after the end of the program
except KeyboardInterrupt:
    print('\nScript end!')
finally:
    GPIO.cleanup()



# mevis jesper.buske@recog.se Variety4-Tinfoil5-Tweet1-Imitation5 https://growcode.mevisio.com/boards/recog/sensordata/machineUser
### imports ###
import time
import json
import RPi.GPIO as GPIO
from VibrationTracker import VibrationTracker

### init ###
# pi ports
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
DIGITALOUT = 14
GPIO.setup(DIGITALOUT, GPIO.IN)
time.sleep(2)
print('Vibration Sensor script')
# settings and counter
settings_file = "settings.json"
with open(settings_file, "r") as file:
    settings = json.load(file)
    counter = VibrationTracker(settings["sample_time"], settings["avrage_time"], 
                               settings["send_time"], settings["swap_threshold"])

### main ###
try:
    while True:
        is_vibrating = not(GPIO.input(DIGITALOUT)==0)
        counter.update_state(is_vibrating)
        time.sleep(settings["sample_time"])
except KeyboardInterrupt:
    print('\nScript end!')
finally:
    GPIO.cleanup()
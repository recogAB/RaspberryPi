### imports ###
import time
import json
import RPi.GPIO as GPIO
from VibrationTracker import VibrationTracker

def set_pi_ports():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    DIGITALOUT = 14
    GPIO.setup(DIGITALOUT, GPIO.IN)
    time.sleep(2)

def read_vibrations(counter):
    ### main ###
    try:
        is_vibrating = not(GPIO.input(DIGITALOUT)==0)
        counter.update_state(is_vibrating)

def free_pi_ports():
    GPIO.cleanup()
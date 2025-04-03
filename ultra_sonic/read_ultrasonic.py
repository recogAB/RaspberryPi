import time
import RPi.GPIO as GPIO

#parameters
ECHO_PIN = 14
TRIG_PIN = 29

def measure():
    speed_of_sound = 34300
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    start = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        stop = time.time()
    elapsed = stop - start
    distance = (elapsed * speed_of_sound) / 2
    return distance

def measure_average():
    distance1 = measure()
    time.sleep(0.1)
    distance2 = measure()
    time.sleep(0.1)
    distance3 = measure()
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance

GPIO.setmode(GPIO.BCM)
TRIG_PIN = 23
ECHO_PIN = 24
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
print('[Press Ctrl + C to end program!]')
try:
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.5)
    while True:
        distance = measure_average()
        print('Distance: {:5.1f}cm'.format(distance))
        time.sleep(1)
except KeyboardInterrupt:
    print('\nScript end!')
finally:
    GPIO.cleanup()
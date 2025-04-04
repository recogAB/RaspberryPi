from opcua import Server
import datetime
import time
import RPi.GPIO as GPIO
from VibrationTracker import VibrationTracker

### variables ###
GPIO_PORT_IN = 14
SAMPLE_TIME = 0.1

### init ###
# region

#server init
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/daddys/server/")
uri = "http://daddys.opcua.pi"
idx = server.register_namespace(uri)
# Create command object
pi_commands = server.nodes.objects.add_object(idx, "PiCommands")
# Commands (Writable by client)
start_pi = pi_commands.add_variable(idx, "StartPi", False)
stop_pi = pi_commands.add_variable(idx, "StopPi", False)
start_pi.set_writable()
stop_pi.set_writable()
# Create status object (only readable)
pi_states = server.nodes.objects.add_object(idx, "PiStates")
# sens2_status = server.nodes.objects.add_object(idx, "Sens2Status")
is_sens1_shaking = pi_states.add_variable(idx, "Sens1Status", False)
is_pi_running = pi_states.add_variable(idx, "IsRunning", False)
# is_sens2_shaking = sens2_status.add_variable(idx, "Sens2Status", False)
#start
server.start()
print("Server started at opc.tcp://0.0.0.0:4840")

# sens trackers
counter1 = VibrationTracker(sample_time=SAMPLE_TIME, avrage_time=5, send_time=60, swap_threshold=0.7)
#it will create issues that I init this one here before we controll start and stop but we leave it for now
# endregion 

try:
    while True:
        # Check commands
        if stop_pi.get_value():
            GPIO.cleanup()
            is_pi_running.set_value(False)
            stop_pi.set_value(False)

        if start_pi.get_value():
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            DIGITALOUT = 14
            GPIO.setup(DIGITALOUT, GPIO.IN)
            time.sleep(2)
            is_pi_running.set_value(True)
            start_pi.set_value(False)

        #update_states
        if is_pi_running.get_value():
            try:
                is_vibrating = not(GPIO.input(DIGITALOUT)==0)
                counter1.update_state(is_vibrating)
                is_sens1_shaking.set_value(counter1.is_machine_on)
            except KeyboardInterrupt:
                print('\nScript end!')

        print(is_sens1_shaking.get_value())
        time.sleep(SAMPLE_TIME)

finally:
    server.stop()

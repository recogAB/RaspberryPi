# this file is just to create som machine data in meviso so that I can view how it looks

import requests
import time
import random
from datetime import datetime, timedelta

def send_state(data):
        url = "https://growcode.mevisio.com/endpoints/recieveSensorData"
        headers = {
            "Authorization": "Bearer ba00d3f7a550439fa940d5fd6acaa57f",
            "Content-Type": "application/json"
        }
        response = requests.post(
            "https://growcode.mevisio.com/endpoints/recieveSensorData",
            json=data,
            headers={
                "Authorization": "Bearer ba00d3f7a550439fa940d5fd6acaa57f",
                "Content-Type": "application/json"
            }
        )
        print("Sending over current state to Mevisio:")
        print("     Status code:", response.status_code)
        print("     Response text:", response.text)

### init ###
delta_time = 2 #[h]
nr_machines = 3
chance_to_flip_state_per_timestep = 0.3
start_time = datetime.now() - timedelta(days=5)
end_time = datetime.now() - timedelta(days=3)

### main ###
loop_time = start_time
current_state_machine = nr_machines*[True]
while end_time > loop_time:
    for machine in range(nr_machines):
        if random.random() < chance_to_flip_state_per_timestep and loop_time != start_time:
        # if True:
             current_state_machine[machine] = not current_state_machine[machine]
             print("swap")
        api_dict = {
            "sensorId": str(machine),
            "sensorType": "vibration",
            "sensorValue": int(current_state_machine[machine]),
            "timeStamp": loop_time.isoformat(),
            "machineId": str(machine),
            "raspberryPiId": "1",
            "team": "the speedy team"
        }
        send_state(api_dict)
        time.sleep(1)
    loop_time = loop_time + timedelta(hours=delta_time)
    
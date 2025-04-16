# this file is just to create som machine data in meviso so that I can view how it looks

import requests
from datetime import datetime, timedelta, time as dt_time
import time  # <-- this is the module that has time.sleep
import random
from datetime import datetime, timedelta
from datetime import timezone
import pytz  # make sure you have this installed

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
delta_time = 1 #[h]
nr_machines = 3
chance_to_flip_state_per_timestep = 0.4

local_tz = pytz.timezone("Europe/Stockholm")
base_date = datetime.now(local_tz).date()
start_time = local_tz.localize(datetime.combine(base_date, dt_time(6, 0)))
end_time = local_tz.localize(datetime.combine(base_date, dt_time(20, 0)))

print(start_time)
### main ###
loop_time = start_time
current_state_machine = nr_machines*[True]
while end_time > loop_time:
    print(loop_time)
    for machine in range(nr_machines):
        if random.random() < chance_to_flip_state_per_timestep and loop_time != start_time:
        # if True:
             current_state_machine[machine] = not current_state_machine[machine]
             print("swap")
        api_dict = {
            "sensorId": str(machine),
            "sensorType": "vibration",
            "isMachineOn": current_state_machine[machine],
            "timeStamp": loop_time.isoformat(),
            "machineId": str(machine),
            "raspberryPiId": "1",
            "team": "the speedy team"
        }
        send_state(api_dict)
        time.sleep(1)
    time.sleep(4)
    loop_time = loop_time + timedelta(hours=delta_time)
    
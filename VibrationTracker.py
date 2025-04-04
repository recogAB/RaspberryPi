from datetime import datetime
import requests

class VibrationTracker:
    def __init__(self, sample_time, avrage_time, send_time, swap_threshold):
        '''sample_time - is time between it checks state in [s].
           avrage_time - is how long time back it avraged over in [s].
           send_time   - is the time between it sends over results to Mevisio in [s].
           swap_threshold - is a fraction that describes the sensitivity 
           of changing vibration state between [0.5-1] 
           where 0.5 is changing state easier and 1 is changing state harder.
        '''
        self.counter = 0
        self.sample_ticks = int(avrage_time/sample_time)
        self.vib_state_list = self.sample_ticks*[False]
        self.send_ticks = int(send_time/sample_time)
        self.is_machine_on = False
        self.send_time = send_time
        self.swap_threshold = swap_threshold
        pass

    def update_state(self, is_vibrating):
        list_counter = self.counter % self.sample_ticks
        self.vib_state_list[list_counter] = is_vibrating
        self.update_machine_state()
        self.counter += 1
        if self.counter % self.send_ticks == 0:
            self.send_state()
        if self.counter >= self.sample_ticks*self.send_ticks:
            self.counter = 0
        
    def update_machine_state(self):
        num_vibrations = sum(self.vib_state_list)
        frac = num_vibrations/self.sample_ticks
        if frac >= self.swap_threshold:
            self.is_machine_on = True
        elif 1 - frac >= self.swap_threshold:
            self.is_machine_on = False

    def send_state(self):
        url = "https://growcode.mevisio.com/endpoints/recieveSensorData"
        headers = {
            "Authorization": "Bearer ba00d3f7a550439fa940d5fd6acaa57f",
            "Content-Type": "application/json"
        }
        data = {
            "sensorId": "Test Pi",
            "sensorType": "Vibration",
            "sensorValueString": "",
            "sensorValueNumber": int(self.is_machine_on),
            "timeStamp": datetime.now().isoformat()
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
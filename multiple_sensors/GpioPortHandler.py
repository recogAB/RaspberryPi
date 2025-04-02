import RPi.GPIO as GPIO

class MultiplexerHandler:
    def __init__(self, controll_out_ports, num_sensors):
        '''controll_out_ports - is a list of ints with GPIO ports id 
        that are connected to the multiplexer controll, the order should be the controll order.
           num_sensors        - is how manny chanels of the multiplexer that are used.
        '''
        self.controll_out_ports = controll_out_ports
        self.num_sensors = num_sensors
        self.active_sensor = 0
        # init ports to sensor
        sensor_to_port_matrix = []
        for i_sensor in range(self.num_sensors):
            binary_str = format(i_sensor, f'0{len(self.controll_out_ports)}b')
            bit_list = [int(bit) for bit in binary_str]
            sensor_to_port_matrix.append(bit_list)
        self.sensor_to_port_matrix = sensor_to_port_matrix
        # init ports
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        #try:
        for port in controll_out_ports:
            GPIO.setup(port, GPIO.IN)
            GPIO.output(port, GPIO.LOW)
        # else port is probably in use

    def set_port
        

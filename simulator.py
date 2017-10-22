class Simulator:
    def __init__(self, sensors):
        self.sensors = sensors
    def get_sensor_sim_data(self):
        return self.sensors
    def set_control_data(self,controls):
        self.controls=controls
    def update(self):
        #update sensor data

class Rocket:
    def __init__(self):
        self.controls = Controls()
    def set_sensor_sim_data(self,sensors):
        self.sensors=sensors
    def get_control_data(self):
        return self.control_data
    def update(self):
        #do stuff with sensors to decide control data

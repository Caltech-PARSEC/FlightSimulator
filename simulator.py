import sensors
class Simulator:
    def __init__(self):
		#initialize self.sensors here
        self.sensors = {'altitude': 0}
    def get_sim_sensors(self):
        return self.sensors
    def update(self, thrust):
        #update sensor data
        pass
    def done(self):
        return False

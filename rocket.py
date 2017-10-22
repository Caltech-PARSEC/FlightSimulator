import sensors
class Rocket:
    def __init__(self):
        self.thrust = 4000 #newtons
    def update(self, sensors):
        #do stuff with sensors to decide thrust
        pass
    def get_thrust(self):
        return self.thrust

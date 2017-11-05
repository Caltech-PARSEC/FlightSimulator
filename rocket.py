import sensors
class Rocket:
    FT_TO_M= 3.28084
    HEIGHT_GOAL = 45000 * FT_TO_M
    def __init__(self):
        self.thrust = 4000 #newtons
    def update(self, sensors):
        if(sensors.get('altitude')>HEIGHT_GOAL)
            self.thrust=0
    def get_thrust(self):
        return self.thrust

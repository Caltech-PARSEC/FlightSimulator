import time
import scipy

class Rocket:
    """
    Implements controls for the rocket to control its ascent. Can work
    either using simulated or real sensor data passed to the update function.
    """

    FT_TO_M= 3.28084
    HEIGHT_GOAL = 45000.0 * FT_TO_M
    VELOCITY_AVERAGING_NUMBER = 5

    def __init__(self, simulated):
        self.thrust = 4000.0 #newtons
        self.first_update = True
        self.simulated = simulated
        self.velocities = [0.0] * self.VELOCITY_AVERAGING_NUMBER
        self.altitude=0.0

    def update(self, sensors):
        self.last_altitude=self.altitude
        self.altitude = sensors.get('altitude')
        if self.__get_height_if_cut() >= self.HEIGHT_GOAL :
            self.thrust=0

    def __get_height_if_cut(self):
        v = self.__get_velocity__()
        t = v/scipy.g
        return -scipy.g/2.0*(t**2)+v*t+self.altitude

    def __get_velocity__(self):
        velocity_sum=0
        for i in range(1,len(self.velocities)):
            self.velocities[i-1] = self.velocities[i]
            velocity_sum += self.velocities[i]
        self.velocities[len(self.velocities)-1]=(self.altitude-self.last_altitude)/self.__get_dt()
        velocity_sum += self.velocities[len(self.velocities)-1]
        return velocity_sum/len(self.velocities)

    def __get_dt(self,sensors):
        if self.simulated:
            self.dt = sensors.get(dt,0.0)
            return
        if self.first_update:
            self.first_update = False
            self.dt=0.0
            self.time = time.perf_counter()
        else:
            self.time_last=self.time
            self.time = time.perf_counter()
            self.dt = self.time - self.time_last

    def get_thrust(self):
        return self.thrust

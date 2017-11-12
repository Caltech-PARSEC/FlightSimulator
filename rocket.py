import time
import scipy.constants as constants

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
        '''
        Updates the rocket's altitude and thrust. If the expected height that would be reached
        if thrust was set to 0 is at least the goal height, thrust is set to 0.

        Arguments:
            sensors: A dictionary contianing the key 'altitude'.
        Return value: None.
        '''

        self.last_altitude=self.altitude
        self.altitude = sensors.get('altitude')
        if self.__get_height_if_cut__(sensors) >= self.HEIGHT_GOAL :
            self.thrust=0

    def __get_height_if_cut__(self, sensors):
        '''
        Estimates the hieght the rocket would reach if thrust was set to zero. Currently it
        only accounts for gravity.

        Arguments:
            sensors: A dictionary containing the key 'dt' for a small time change.
        Return value: A float representing the estimated max hieght if thrust = 0.
        '''

        v = self.__get_velocity__(sensors)
        t = v / constants.g
        return -constants.g / 2.0 * (t ** 2) + v * t + self.altitude

    def __get_velocity__(self, sensors):
        '''
        Finds and returns the velocity of the rocket. The last 'VELOCITY_AVERAGING_NUMBER' 
        velocities are kept track of and the current velocity is calculated by dividing the
        difference in altitude where it was one 'dt' before and what altitude it is at now
        by the time difference, 'dt'. However, the averge of the last 'VELOCITY_AVERAGING_NUMBER'
        velocities is returned, not the one calculated using differnce in height divided by 
        difference in time.

        Arguments:
            sensors: A dictionary containing the key 'dt' for a small time change.
        Return value: A float representing the velocity of the rocket.
        '''

        # Variable to keep track of the sum of the last 'VELOCITY_AVERAGING_NUMBER' velocities
        velocity_sum = 0

        for i in range(1, len(self.velocities)):
            # Move each stored velocity one place back in the list and update the sum
            self.velocities[i-1] = self.velocities[i]
            velocity_sum += self.velocities[i]

        # Calculate the current velocity using change in distance divided by change in time
        self.velocities[len(self.velocities)-1] = (self.altitude - self.last_altitude) / \
                self.__get_dt__(sensors)

        # Add the current velocity to the list of velocities
        velocity_sum += self.velocities[len(self.velocities)-1]

        # Return the average velocity of those kept track of
        return velocity_sum / len(self.velocities)

    def __get_dt__(self, sensors):
        '''
        Returns 'dt', which is the time (in seconds) between calls to the update function. If 
        the rocket is being simulated, 'dt' is retrieved from a dictionary passed as the argument
        or set to 0.0 if the dictionary does not contain the key 'dt'.

        Arguments:
            sensors: A dictionary which may contain the key 'dt'.
        Return value: A float representing 'dt'.
        '''

        if self.simulated:
            self.dt = sensors.get('dt', 0.0)
            return self.dt
        if self.first_update:
            self.first_update = False
            self.dt=0.0
            self.time = time.perf_counter()
        else:
            self.time_last=self.time
            self.time = time.perf_counter()
            self.dt = self.time - self.time_last

        return self.dt

    def get_thrust(self):
        '''
        Arguments:
            None
        Return value: A float representing the rocket's thrust.
        '''

        return self.thrust

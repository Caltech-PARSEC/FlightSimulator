import os
import json


class Simulator:
    def __init__(self, param_file='parameters.json'):
		'''initialize self.sensors here based on values in the parameters.json file'''
        
        self.load_data(param_file)

    def load_data(self, param_file):
        ''' Sets path to look for parameters file in current directory''' 
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
        with open(os.path.join(__location__,param_file), 'r') as inputf:
            self.parameters = json.load(inputf)

        # Set imported parameters as properties
        for parameter in self.parameters:
            setattr(self, parameter, self.parameters[parameter])        

       
        self.velocity = 5
        self.velocities = [5]
        self.altitude = self.launch_altitude
        self.altitudes = [self.altitude]
        self.acceleration = 0
        self.fuel = [self.initial_fuel]

        self.max_altitude = 0 
        self.max_velocity = 0
        self.max_acceleration = 0
        self.initial_fuel = 5

        self.mass = self.launch_mass

        self.sensors = {'altitude': self.altitude, 'dt': self.dt}

    def get_fuel_remaining(self):
        '''returns the next fuel remaining amount '''
        fuel_remaining = self.fuel[-1] - self.get_fuel_rate(dt) * self.dt
        self.fuel.append(fuel_remaining)
        return fuel_remaining 

    def get_altitude(self):
        ''' Returns current altitude by retrieving from the altitudes list'''
        return self.altitudes[len(self.altitudes)]

    def get_fuel_rate(self, time):
        '''Returns current fuel rate'''
        return 5

    def update_altitude(self):
        '''Updates the altitude for time interval dt with current velocity. Adds current altitude to the
        altitudes list, and to the sensors dictionary'''

        self.altitude = self.altitudes[-1] + self.velocity * self.dt
        self.altitudes.append(self.altitude)
        self.sensors['altitudes'] = self.altitude

    def update_velocity(self, thrust, air_density, area):
        '''Updates the velocity of the rocket for time interval dt'''
        drag = area * self.rocket_drag_coef * air_density * (self.velocity ** 2) / 2
        f_grav = self.mass * 9.8

        delta_v = (thrust - drag - f_grav) * self.dt / self.mass
        self.velocity += delta_v

    def get_sim_sensors(self):
        return self.sensors

    def update(self, thrust):
        '''
        Update the sensor data and the rocket's attributes.
        '''

        self.update_velocity(thrust, self.air_density, self.cross_area)
        self.update_altitude()

        print(f'velocity: {self.velocity}, alt: {self.altitude}')

    def done(self):
        return self.velocity < 0

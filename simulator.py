import os
import json
import numpy

class Simulator:
    def __init__(self, param_file='parameters.json'):
		#initialize self.sensors here
        
        self.load_data(param_file)

    def load_data(self, param_file):
        # In order to make sure to look for parameters file in current directory 
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
        

        self.max_altitude = 0 
        self.max_velocity = 0
        self.max_acceleration = 0
        self.initial_fuel = 5

        self.mass = self.launch_mass

        self.sensors = {'altitude': self.altitude, 'dt': self.dt}

    def get_fuel_remaining(self):
        fuel_remaining = velocities[len(velocities)] - self.get_fuel_rate(dt) * self.dt
        velocities.append(fuel_remaining) 

    def get_altitude(self):
        return self.altitudes[len(self.altitudes)]

    def get_fuel_rate(self, time):
        return 5

    def update_altitude(self):
        self.altitude = self.altitudes[-1] + self.velocity * self.dt
        self.altitudes.append(self.altitude)

    def update_velocity(self, thrust, air_density, area):
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

    def done(self):
        return False

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
        self.altitude = self.launch_altitude
        self.acceleration = 0
        

        self.max_altitude = 0 
        self.max_velocity = 0
        self.max_acceleration = 0
        self.initial_fuel = 5

        self.mass = self.launch_mass

        self.sensors = {'altitude': self.altitude, 'dt': self.dt}

    def get_fuel_remaining(self, time):
        fuelRemaining = self.initial_fuel
        for interval in numpy.arange(0.0, time, self.dt): #dt gotten from param file
            fuelRemaining -= self.get_fuel_rate(interval) * self.dt
            if fuelRemaining <= 0:
                print("Out of fuel at height:" + str(self.get_altitude(interval)))
                return
        return fuelRemaining

    def get_altitude(self, time):
        self.update_altitude(time)
        return self.altitude


    def get_fuel_rate(self, time):
        return 5

    def update_altitude(self, time):
        self.altitude = self.launch_altitude + self.velocity * time

    def update_velocity(self, thrust, air_density, area):
        g = 9.8 
        drag = area * self.rocket_drag_coeff * air_density * \
               (self.velocity ** 2) / 2
        f_grav = self.mass * g

        delta_v = (thrust - drag - f_grav) * self.dt / self.mass
        self.velocity += delta_v

    def get_sim_sensors(self):
        return self.sensors

    def update(self, thrust):
        #update sensor data
        pass

    def done(self):
        return False

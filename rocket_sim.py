import os
import json
import numpy
class RocketSimulator(object):
   
        
    def __init__(self, param_file='parameters.json'):
        
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
        self.height = self.launch_height
        self.acceleration = 0
        

        self.max_height = 0 
        self.max_velocity = 0
        self.max_acceleration = 0
        self.initial_fuel = 5

        self.mass = self.launch_mass

        
        # creating a dictionary to hold values if needed #
        self.data = {}
        self.data['time'] = []
        self.data['height'] = []
        self.data['velocity'] = []
        self.data['acceleration'] = []       
        
        

    def getFuelRate(self, time):
        return 5
        #pass
    
    # gets oxidizer rate    
    def getOxiRate(self, time):
        pass
    
    def getFuelRemaining(self, time):
        fuelRemaining = self.initial_fuel
        for interval in numpy.arange(0.0, time, self.dt): #dt gotten from param file
            fuelRemaining -= self.getFuelRate(interval) * self.dt
            if fuelRemaining <= 0:
                print("Out of fuel at height:" + str(self.getHeight(interval)))
                return
        return fuelRemaining
        
    def getHeight(self, time):
        self.updateHeight(time)
        return self.height
   
    def getSensorSimData():
        pass
    
    def setControlData(control):
        pass
    
    def updateHeight(self, time):
        self.height = self.launch_height + self.velocity * time #placeholder
         
           
           
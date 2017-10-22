class Sensors:

    def __init__(self, init_values):
        '''The constructor accepts a dictionary of initial values for the
        sensors and sets adds to keys/values to sensor_values.'''
        for key in init_values:
            self.sensor_values[key] = init_values[key]
            print(self.sensor_values[key])
            #sensor_values

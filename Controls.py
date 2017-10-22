class Controls:
    def __init__(self):
        self.controls_values = {
                'Engine On':true
                'Drogue Parachute Deployed':false
                'Main Parachute Deployed':false
        }
    def set_control_value(self, key, value):
        self.controls_values[key]=value
    def get_control_values(self):
        return self.controls_values

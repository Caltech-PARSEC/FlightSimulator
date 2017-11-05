from simulator import *
import nose

def test_get_altitude():
    for time in range(max_time):
        assert(sim.get_altitude(time) >= 0)

def test_get_fuel_rate():
    for time in range(max_time):
        assert(sim.get_fuel_rate(time) >= 0)

def test_update_altitude():
    for time in range(max_time):
        sim.update_altitude(time)
        assert(sim.altitude >= 0)

if __name__ == '__main__':
    sim = Simulator()
    max_time = 100 # arbitrary value
    nose.runmodule()

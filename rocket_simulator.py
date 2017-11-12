from rocket import Rocket
from simulator import Simulator

def main():
    rocket = Rocket(True)
    simulator = Simulator()

    while not simulator.done():
        simulator.update(rocket.get_thrust())
        rocket.update(simulator.get_sim_sensors())
        print(f'Thrust: {rocket.get_thrust()}')

if __name__ == '__main__':
    main()

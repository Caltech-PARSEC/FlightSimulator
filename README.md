# FlightSimulator

## Overview

The goal of this project is to create a simulator for our rocket, which will allow us to test different cotrol algorithms on our rocket, as well as to determine how much fuel and oxidizer will be necessary for our rocket to reach 45,000 ft.

### Project Goals

#### Milestrone One - Basic Differential Equation Simulation

- Simulator that takes in amount of thrust output and returns a new rocket state
- Rocket Controller class that takes in a rocket state and determines the amount of thrust to output
- Rocket Simulator Interface Class that passes information between the two objects to run a simulation
- Result of simulation is output in some graphable format, with each point plotted via time
- Simulation done using very basic diff eq (e.g. account for current velocity and get new acceleration)

#### Milestone Two - Better Equations

- Simulator uses differential equation developed by Aeronautics team
- Simulator adds in information about weather conditions
- Simulator adds some random noise to each step (e.g. wind, turbulence, etc)

#### Milestone Three - More Variables and Data Returned

- Simulator can predict amount of fuel required to reach 45,000 ft apogee.
- Simulator accounts for more variables in flight


from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def run_anglerfish(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=100)
    # go straight off base. 
    # close but not touch artificial habitab
    robot.straight(200)
    # turn right a bit to head to right of anglerfish
    robot.turn(-30)
    robot.straight(500)
    # turn right toward the cold sea 
    robot.turn(-48)
    # go to cold sea so octopus land in the sea
    robot.straight(160)
    # come back a bit to leave octopus in the sea
    robot.straight(-150)
    # turn left to align with anglerfish
    robot.turn(35)
    # go straight to push the latch
    robot.straight(500)
    # stop there. end of game





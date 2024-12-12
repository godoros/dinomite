
from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def run_anglerfish(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=100)
    robot.straight(200)
    robot.turn(-30)
    robot.straight(500)
    robot.turn(-52)
    robot.straight(160)
    robot.straight(-150)
    robot.turn(40)
    robot.straight(300)





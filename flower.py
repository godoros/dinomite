
from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def runFlower(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    # robot.settings(straight_speed=300)
    # robot.straight(1000)
    # wait(100)
    # robot.straight(-100)
    # wait(100)
    # rmotor.run_time(speed=-500, time=500)
    # rmotor.run_angle(speed=300, rotation_angle=-90)
    robot.settings(straight_speed=300)
    robot.straight(600)
    robot.straight(-200)
    robot.turn(-50)
    robot.straight(1500)














from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def run_coral_nursery(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    robot.settings(straight_speed=350, turn_rate=100)
    robot.straight(490)
    robot.turn(-45)
    robot.straight(250)
    robot.turn(140)
    robot.straight(300)
    """robot.straight(-270)
    robot.turn(-150)
    robot.straight(-800)"""
    robot.straight(-230)
    robot.turn(-30)
    robot.straight(350)
    robot.straight(-150)
    robot.turn(110)
    robot.settings(straight_speed=500)
    robot.straight(800)
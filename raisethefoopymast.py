from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def raiseFoopyMast(hub: PrimeHub, robot: DriveBase):
    robot.settings(straight_speed=300)
    robot.straight(490)
    robot.settings(straight_speed=350, turn_rate=100)
    robot.turn(-85)
    robot.straight(100) 
    robot.settings(straight_speed=100)
    robot.straight(175)
    robot.straight(-140)
    robot.turn(45)
    robot.settings(straight_speed=450)
    robot.straight(-2000)













from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def raiseFoopyMast(hub: PrimeHub, robot: DriveBase):
    robot.settings(straight_speed=300)
    robot.straight(400)
    robot.turn(-25)
    robot.straight(125)
    robot.turn(-65)
    robot.settings(straight_speed=350, turn_rate=100)
    robot.straight(100) 
    robot.settings(straight_speed=100)
    robot.straight(150)
    robot.straight(-140)
    robot.turn(45)
    robot.settings(straight_speed=450)
    robot.straight(-600)













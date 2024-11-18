
from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def shrimpRight(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300)
    robot.straight(150)
    robot.turn(45)
    robot.straight(200)
    robot.turn(-45)
    robot.straight(150)
    robot.turn(40)
    robot.straight(150)
    robot.turn(-90)
    robot.straight(60)
    robot.turn(90)
    robot.straight(200)
    robot.straight(-850)
def whale_eats(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=100)
    robot.straight(675)
    robot.turn(-45)
    robot.straight(280)
    robot.straight(-280)
    robot.turn(45)
    robot.straight(-750)









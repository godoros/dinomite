from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def shrimpLeft(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=350)
    robot.straight(230)
    robot.turn(-45)
    robot.straight(120)
    robot.turn(45)
    robot.straight(100)
    robot.turn(-15)
    robot.straight(120)
    robot.turn(20)
    robot.straight(350)
    robot.straight(-420)
    robot.turn(-45)
    robot.straight(-500)
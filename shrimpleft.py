from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def shrimpLeft(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=350)
    robot.straight(230)
    robot.turn(-65)
    robot.straight(130)
    robot.turn(80)
    robot.straight(100)
    robot.turn(-35)
    robot.straight(130)
    robot.turn(40)
    robot.straight(400)
    robot.straight(-420)
    robot.turn(-45)
    robot.straight(-500)
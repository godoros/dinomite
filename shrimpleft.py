from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def shrimpLeft(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=100)
    robot.straight(230)
    robot.turn(-45)
    robot.straight(130)
    robot.turn(38)
    robot.straight(100)
    robot.turn(-5)
    robot.straight(130)
    robot.turn(15)
    robot.settings(straight_speed=200)
    robot.straight(350)
    robot.settings(straight_speed=400)
    robot.straight(-600)
    robot.turn(-50)
    robot.straight(-450)
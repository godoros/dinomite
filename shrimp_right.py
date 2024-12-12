
from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def shrimpRight(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=100)
    robot.straight(150)
    robot.turn(45)
    robot.straight(200)
    robot.turn(-40)
    robot.straight(150)
    robot.turn(10)
    robot.straight(150)
    robot.turn(-45)
    robot.straight(70)
    robot.turn(30)
    robot.straight(300)
    robot.settings(straight_speed=500)
    robot.straight(-850)

def whale_eats(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=50)
    robot.straight(665)
    robot.turn(-45)
    robot.straight(300)
    robot.settings(straight_speed=100)
    robot.straight(-50)
    robot.settings(straight_speed=350, turn_rate=200)
    robot.straight(-230)
    robot.turn(45)
    robot.straight(-400)
    robot.turn(45)
    robot.settings(straight_speed=400)
    robot.straight(-350)









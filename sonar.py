
from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def runSonar(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=100)
    robot.straight(240)
    robot.turn(30)
    robot.straight(505)
    robot.turn(-30)
    robot.straight(200)
    lmotor.run_angle(speed=300, rotation_angle=720) 
    robot.straight(-610)
    robot.turn(45)
    robot.straight(300)
    robot.straight(-800)













from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def runSonar(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(straight_speed=300, turn_rate=100)
    robot.straight(240)
    robot.turn(30)
    robot.straight(515)
    robot.turn(-25)
    robot.straight(170)
    lmotor.run_angle(speed=300, rotation_angle=800) 
    robot.straight(-580)
    robot.turn(45)
    robot.straight(260)
    robot.straight(-800)












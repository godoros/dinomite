
from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def runSonar(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    robot.settings(turn_rate=200)
    robot.straight(240)
    robot.turn(30)
    robot.straight(510)
    robot.turn(-30)
    robot.straight(145)
    lmotor.run_angle(speed=300, rotation_angle=850) 
    robot.straight(-580)
    robot.turn(45)
    robot.straight(250)
    robot.straight(-800)












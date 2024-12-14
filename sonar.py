
from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def runSonar(hub: PrimeHub, robot: DriveBase, lmotor: Motor):
    # relatively fast go straight and slower turn
    robot.settings(straight_speed=300, turn_rate=100)
    # go forward a bit
    robot.straight(240)
    # turn left 30 degrees
    robot.turn(30)
    # go forward (diagonally) and stop before sonar
    robot.straight(500)
    # turn right to make it straight 12'o clock direction
    robot.turn(-30)
    # go forward to align with sonar
    robot.straight(200)
    # rotate arm to flip both flippers
    lmotor.run_angle(speed=300, rotation_angle=750) 
    # come back
    robot.straight(-610)
    # turn right a bit to head towrad octopus
    robot.turn(45)
    # push forward to make octopus drop
    robot.straight(300)
    # back to base
    robot.straight(-700)












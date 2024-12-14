from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def raiseFoopyMast(hub: PrimeHub, robot: DriveBase):
    robot.settings(straight_speed=300)
    # go forward and stop before nursury
    robot.straight(400)
    # turn right a bit to avoid nursery
    robot.turn(-25)
    # forward diagonally to aligh with mast
    robot.straight(125)
    # turn right toward mast
    robot.turn(-65)
    robot.settings(straight_speed=350, turn_rate=100)
    # get close to mask and stop before touching it
    robot.straight(100) 
    #  make it slower to avoid over flip mast
    robot.settings(straight_speed=100)
    # forward to lift mast
    robot.straight(150)
    # backward to leave mast alone
    robot.straight(-140)
    # turn left to align with base direction
    robot.turn(45)
    # raise speed
    robot.settings(straight_speed=450)
    # back to base
    robot.straight(-600)













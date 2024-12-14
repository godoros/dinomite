from pybricks.pupdevices import Motor, 
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def run_coral_nursery(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    robot.settings(straight_speed=350, turn_rate=100)
    # go forward and stop before nursery
    robot.straight(490)
    # turn right a bit to avoid hitting nursery
    robot.turn(-45)
    # forward a bit to aligh with nursery
    robot.straight(250)
    # turn to head nursery direction
    robot.turn(140)
    # push down nursery bar to flip buds up
    robot.straight(300)
    # back to middle
    robot.straight(-230)
    # turn right a bit to head toward shark
    robot.turn(-30)
    # forward to push shark bar
    robot.straight(350)
    # backward to middle 
    robot.straight(-150)
    # turn to base direction
    robot.turn(110)
    # max speed
    robot.settings(straight_speed=500)
    # back to base
    robot.straight(800)
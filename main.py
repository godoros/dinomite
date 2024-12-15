from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu


from setup import setup
from raisethefoopymast import raiseFoopyMast
from sonar import *
from shrimp_right import *
from shrimpleft import *
from flower import *
from testutil import *
from coral_nursery import *
from anglerfish import *

def waitKey(hub: PrimeHub):
    while True:
        pressed = hub.buttons.pressed()
        if pressed:
            return
        wait(10)


def goAcross(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    robot.settings(straight_speed=300)
    robot.straight(600)
    robot.straight(-200)
    robot.turn(-45)
    robot.settings(straight_speed=500)
    robot.straight(650)
    robot.turn(-25)
    robot.straight(650)


def runAll(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    shrimpLeft(hub, robot, lmotor)
    waitKey(hub)
    run_coral_nursery(hub, robot, lmotor, rmotor)
    waitKey(hub)
    raiseFoopyMast(hub, robot)
    waitKey(hub)
    goAcross(hub, robot, lmotor, rmotor)
    waitKey(hub)
    shrimpRight(hub, robot, lmotor)
    waitKey(hub)
    runSonar(hub, robot, lmotor)
    waitKey(hub)
    whale_eats(hub, robot, lmotor)
    waitKey(hub)
    run_anglerfish(hub, robot, lmotor)

def runAllRight(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    shrimpRight(hub, robot, lmotor)
    waitKey(hub)
    runSonar(hub, robot, lmotor)
    waitKey(hub)
    whale_eats(hub, robot, lmotor)
    waitKey(hub)
    run_anglerfish(hub, robot, lmotor)

def runStartFromCross(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    goAcross(hub, robot, lmotor, rmotor)
    waitKey(hub)
    runAllRight(hub, robot, lmotor, rmotor)

hub, robot, lmotor, rmotor = setup()
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

while True:
    # define a menu. this shows up on primehub display.
    # use left/right arrow to switch and center button to accept
    sel = hub_menu("Z", "A", "T", "0", "L", "R", "M", "1", "2", "3", "4", "5", "6", "7", "8")
    if sel == "Z":
        # exit program
        break
    elif sel == "A": 
        # run all missions one by one. press any button to goto next mission.
        runAll(hub, robot, lmotor, rmotor)
    elif sel == "T": 
        # run all the missions on the right of table
        runAllRight(hub, robot, lmotor, rmotor)
    elif sel == "0": 
        # start from left to go cross
        runStartFromCross(hub, robot, lmotor, rmotor)
    elif sel == "L": 
        # test to rotate left motor
        testLeftMotor(hub, lmotor)
    elif sel == "R":
        # test to rotate right motor
        testLeftMotor(hub, rmotor)
    elif sel == "M":
        # go forward and come back
        testBackAndForth(hub, robot)
    elif sel == "1":
        # collect all krills on the left of table
        shrimpLeft(hub, robot, lmotor)
    elif sel == "2":
        # coral_nursery and shark
        run_coral_nursery(hub, robot, lmotor, rmotor)
    elif sel == "3":
        # mast mission
        raiseFoopyMast(hub, robot)
    elif sel == "4":
        # cross the table from left to right
        goAcross(hub, robot, lmotor, rmotor)
    elif sel == "5":
        # collect all krills on the right
        shrimpRight(hub, robot, lmotor)
    elif sel == "6":
        # sonar mission
        runSonar(hub, robot, lmotor)
    elif sel == "7":
        # whale mission
        whale_eats(hub, robot, lmotor)
    elif sel == "8":
        # anglerfish mission
        run_anglerfish(hub, robot, lmotor)
    elif sel == "9":
        runFlower(hub, robot, lmotor, rmotor)
print("done")


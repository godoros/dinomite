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
    robot.turn(-50)
    robot.straight(1200)


def runAll(hub: PrimeHub, robot: DriveBase, lmotor: Motor, rmotor: Motor):
    shrimpLeft(hub, robot, lmotor)
    waitKey(hub)
    raiseFoopyMast(hub, robot)
    waitKey(hub)
    run_coral_nursery(hub, robot, lmotor, rmotor)
    waitKey(hub)
    goAcross(hub, robot, lmotor, rmotor)
    waitKey(hub)
    shrimpRight(hub, robot, lmotor)
    waitKey(hub)
    runSonar(hub, robot, lmotor)
    waitKey(hub)
    whale_eats(hub, robot, lmotor)


hub, robot, lmotor, rmotor = setup()
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

while True:
    sel = hub_menu("Z", "A", "L", "R", "M", "1", "2", "3", "4", "5", "6", "7", "8")
    if sel == "Z":
        break
    elif sel == "A": 
        runAll(hub, robot, lmotor, rmotor)
        # runSonar(hub, robot, lmotor)
    elif sel == "L": 
        testLeftMotor(hub, lmotor)
    elif sel == "R":
        testLeftMotor(hub, rmotor)
    elif sel == "M":
        testBackAndForth(hub, robot)
    elif sel == "1":
        raiseFoopyMast(hub, robot)
    elif sel == "2":
        runSonar(hub, robot, lmotor)
    elif sel == "3":
        shrimpRight(hub, robot, lmotor)
    elif sel == "4":
        whale_eats(hub, robot, lmotor)
    elif sel == "5":
        shrimpLeft(hub, robot, lmotor)
    elif sel == "6":
        runFlower(hub, robot, lmotor, rmotor)
    elif sel == "7":
        run_coral_nursery(hub, robot, lmotor, rmotor)
    elif sel == "8":
        run_anglerfish(hub, robot, lmotor)
print("done")


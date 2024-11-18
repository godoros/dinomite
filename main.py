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
from testutil import *

hub, robot, lmotor, rmotor = setup()
# we use center button as the commit/accept instead of terminating the program.
# instead, press center and bluetooth buttons together to terminate.
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

# this is the main loop
while True:
    # display a menu, use left/right arrow to switch between menu items.
    # use center button to select/commit the menu item.
    sel = hub_menu("Z", "L", "R", "M", "1", "2", "3", "4", "5")
    if sel == "Z":
        break
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
print("done")


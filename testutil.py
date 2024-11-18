from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction, Button
from pybricks.tools import wait, hub_menu, run_task
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

def testBackAndForth(hub: PrimeHub,  robot: DriveBase):
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            robot.straight(100)
        if Button.RIGHT in pressed:
            robot.straight(-100)
        if Button.CENTER in pressed:
            return
        wait(10)

def testLeftMotor(hub: PrimeHub,  motor: Motor):
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            motor.run_angle(speed=200, rotation_angle=10)
        if Button.RIGHT in pressed:
            motor.run_angle(speed=200, rotation_angle=-10)
        if Button.CENTER in pressed:
            return
        wait(10)

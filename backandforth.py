from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction, Button
from pybricks.tools import wait, hub_menu, run_task
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

hub = PrimeHub()
left_motor = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
leftfront_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightfront_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
# drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).

"""
Set speed:
drive_base.settings(straight_speed=300)

move forward/backward:
drive_base.straight(900)

Wait:
wait(1000)

Turn:
drive_base.turn(90)
"""
# drive_base.straight(900)
# drive_base.turn(90)

# drive_base.settings(straight_speed=100)
# drive_base.straight(200)
# wait(2000)
# drive_base.straight(-200)
# rightfront_motor.run_angle(speed=300, rotation_angle=-250)


async def testButton():
    hub.system.set_stop_button((Button.BLUETOOTH, Button.CENTER))
    sel = hub_menu("1", "2")
    print(sel)
    if sel == "1":
        n = 1
    elif sel == "2":
        n = 2
    hub.display.number(n)
    while not Button.CENTER in hub.buttons.pressed():
        wait(50)
    print("done")

run_task(testButton())



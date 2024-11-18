from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
topleft_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)

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
frlrlrfb
Turn twice and go straight forward
"""

drive_base.settings(straight_speed=350)

drive_base.straight(250)
drive_base.turn(-40)
drive_base.straight(120)
drive_base.turn(40)
drive_base.straight(100)
drive_base.turn(-15)
drive_base.straight(120)
drive_base.turn(15)
drive_base.straight(300)
drive_base.straight(-420)
drive_base.turn(-45)
drive_base.straight(-500)
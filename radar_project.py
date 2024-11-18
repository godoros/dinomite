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
#drive_base.straight(800)
topleft_motor.run_angle(speed=500, rotation_angle=1300) 
#drive_base.straight(-800)
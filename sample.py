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
drive_base.settings(straight_speed=300)
drive_base.straight(900)
# topleft_motor.run_angle(speed=50, rotation_angle=90)
drive_base.straight(-20)
wait(1000)
drive_base.straight(-800)
drive_base.turn(90)
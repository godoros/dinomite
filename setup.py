from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction, Button
from pybricks.tools import wait, hub_menu, run_task
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

def setup(): 

    hub = PrimeHub()
    left_motor = Motor(Port.B, Direction.CLOCKWISE)
    right_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
    leftfront_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    rightfront_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

    # Initialize the drive base. In this example, the wheel diameter is 56mm.
    # The distance between the two wheel-ground contact points is 112mm.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)
    # robot.use_gyro(True)
    return hub, robot, leftfront_motor, rightfront_motor

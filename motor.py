from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix

# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":0,"y":0,"deletable":false,"next":{"block":{"type":"variables_set_motor","id":".pAh!wR#XkHSkZ4kpz@-","fields":{"VAR":{"id":"t$/Bi6A7w#3cTSp~|U:@"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"XkGc.;ka]x:f]*mE_wU}","fields":{"NAME":"E"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"Y={4RhH!]uuhwKI.fJ5)","fields":{"SELECTION":"Direction.COUNTERCLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"d|EHHJn=|:5,#gtJq8mW","fields":{"VAR":{"id":"}50YTbLq/ufog[PA#fYf"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":";I}R#]HyT#]]1zur+Uft","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"F~s`@F*+E}i-vE`J8s78","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_drive_base","id":"D3GLV{Zx/v$t+8h{E|SW","fields":{"VAR":{"id":"E)oU*3nWTdMQ;)%EDPL:"}},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":",!9|zr/2kN:`VasReczH","fields":{"VAR":{"id":"t$/Bi6A7w#3cTSp~|U:@","name":"leftw","type":"Motor"}}}},"VAR2":{"shadow":{"type":"variables_get_motor_device","id":"J)*i[._Vs3pH[i0n4v0J","fields":{"VAR":{"id":"}50YTbLq/ufog[PA#fYf","name":"rightw","type":"Motor"}}}},"VALUE0":{"shadow":{"type":"unit_distance","id":"H`38Z@|8e#JHW-~+BL{v","fields":{"VALUE0":65}}},"VALUE1":{"shadow":{"type":"unit_distance","id":"G7/#*4#Z{tx?})OZ2ZiH","fields":{"VALUE0":85}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":9,"y":241,"deletable":false,"next":{"block":{"type":"blockFlowRepeat","id":"W_vm|~8Mk43~LmKL/7y@","inputs":{"TIMES":{"shadow":{"type":"blockMathNumber","id":",19C+vq=!;i_y+wo#7k%","fields":{"NUM":3}}},"DO":{"block":{"type":"blockDriveBaseDrive","id":"CK;@FeUPu/K2EKt9]bU.","extraState":{"optionLevel":3},"fields":{"METHOD":"DRIVEBASE_DRIVE_TURN"},"inputs":{"VAR":{"shadow":{"type":"variables_get_drive_base_device","id":"lFp}{heH`)~qfoiO7{fi","fields":{"VAR":{"id":"E)oU*3nWTdMQ;)%EDPL:","name":"robot","type":"DriveBase"}}}},"ARG0":{"shadow":{"type":"unit_angle","id":"CI]I5o4iOJ!V=|f9jSX?","fields":{"VALUE0":90}}},"ARG1":{"shadow":{"type":"parameters_stop_4","id":"HD9tIN.HArD^5W7P13H@","fields":{"VALUE":"Stop.HOLD"}}}},"next":{"block":{"type":"blockWaitTime","id":"dSgS7Co[l+ttLBDwN=?O","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":")2GY-[0L:MpgEx`@,o?Z","fields":{"VALUE0":1000}}}}}}}}}}}}]},"variables":[{"name":"red","id":"NKY-3d]Egr$t5XR!R_Mm","type":"ColorDef"},{"name":"orange","id":"9]E]){5lmr;=i([(Ayi:","type":"ColorDef"},{"name":"yellow","id":"TQ:a[p*LZQFCpjHCtmR|","type":"ColorDef"},{"name":"green","id":"[%uk@s:w:tSg@6m38(v_","type":"ColorDef"},{"name":"cyan","id":"*M@mfnnZ7Jkv8+Iv_(L0","type":"ColorDef"},{"name":"blue","id":"~@eIxu6tK]tuIa$L[KLC","type":"ColorDef"},{"name":"violet","id":",8O58e;P2PprkQr3m41@","type":"ColorDef"},{"name":"magenta","id":"%=rdLw*`_UF~^z%A#:e_","type":"ColorDef"},{"name":"white","id":"dpmP(|VR51Sb5?NoZs$R","type":"ColorDef"},{"name":"none","id":"8Pvmo2RZ%`$io5O:$][r","type":"ColorDef"},{"name":"leftw","id":"t$/Bi6A7w#3cTSp~|U:@","type":"Motor"},{"name":"rightw","id":"}50YTbLq/ufog[PA#fYf","type":"Motor"},{"name":"robot","id":"E)oU*3nWTdMQ;)%EDPL:","type":"DriveBase"}],"info":{"type":"pybricks","version":"1.2.3"}}
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
hub = PrimeHub()
leftw = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightw = Motor(Port.A, Direction.CLOCKWISE)
robot = DriveBase(leftw, rightw, 65, 85)


# The main program starts here.
# hub.light.blink(color=Color.RED, durations=[1000,2000])
# for count in range(3):
#     robot.turn(90)
#     wait(1000)
# leftw.run_angle(500, 360)
# leftw.run_target(500, 0)

# robot.drive(500, 500)
# robot.straight(-2000)
# robot.turn(90)
# for i in range(100):
#     hub.display.number(i)
#     wait(1000)

# hub.speaker.beep()

SQUARE = Matrix(
    [
        [100, 100, 100, 100, 100],
        [100, 50, 50, 50, 100],
        [100, 50, 0, 50, 100],
        [100, 50, 50, 50, 100],
        [100, 100, 100, 100, 100],
    ]
)

# Display the square.
hub.display.icon(SQUARE)
wait(3000)

# Make an image using a Python list comprehension. In this image, the
# brightness of each pixel is the sum of the row and column index. So the
# light is faint in the top left and bright in the bottom right.
GRADIENT = Matrix([[(r + c) for c in range(5)] for r in range(5)]) * 12.5

# Display the generated gradient.
hub.display.icon(GRADIENT)
wait(3000)
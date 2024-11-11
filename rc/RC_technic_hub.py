from pybricks.hubs import TechnicHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import Car
from pybricks.tools import multitask, run_task, wait

# set up all devices
#   this is the minimum set-up for RC cars
hub = TechnicHub()
steering = Motor(Port.D, Direction.CLOCKWISE)
drive_1 = Motor(Port.A, Direction.COUNTERCLOCKWISE)
car = Car(steering, drive_1)
xbox = XboxController()

# initialize variables
driveDirection = 1
steerDirection = 1
color = Color.MAGENTA


async def process_buttons():
    global driveDirection, steerDirection
    # This task handles the buttons
    while True:
        await wait(1)
        while not any(xbox.buttons.pressed()):
            await wait(1)
        if Button.X in xbox.buttons.pressed():
            # Switch drive direction
            if driveDirection == 1:
                driveDirection = -1
            else:
                driveDirection = 1
            while Button.X in xbox.buttons.pressed():
                await wait(1)
        elif Button.Y in xbox.buttons.pressed():
            # Switch steering direction
            if steerDirection == 1:
                steerDirection = -1
            else:
                steerDirection = 1
            while Button.Y in xbox.buttons.pressed():
                await wait(1)
        else:
            # Button has no function
            pass

async def drive(color):
    hub.light.on(color)
    while True:
        await wait(1)
        # Control steering using the left joystick
        car.steer(steerDirection * xbox.joystick_left()[0])
        # Control drive power using the trigger buttons
        car.drive_power(driveDirection * xbox.joystick_right()[1])
        await wait(50)

async def main(color):
    await multitask(process_buttons(), drive(color))



# try adding the second drive motor
#   if it's not connected, an error is thrown; simply ignore it
try:
    drive_2 = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    car = Car(steering, [drive_1, drive_2])
    color = Color.CYAN
except OSError:
    pass

run_task(main(color))
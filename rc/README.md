# Remote Control
Collection of code for remote control of LEGO technics builds.

## Generic remote control
Remote control all your LEGO technic builds with an Xbox Controller.

### Functionality
Allows using the same program no matter the car you built.
Enables remote controlling LEGO car builds with 2 or 3 motors and using the Powered Up Bluetooth Hub (aka the technic hub).
The program detects how many motors there are and will drive the motors accordingly. 
 - Use 1 or 2 motors for driving
 - Hit the X button to switch positive direction of motor(s) used for driving
 - Hit the Y button to switch positive direction of motor used for steering

### Requirements
The program remains simple and requires some things to be respected:
 - Pybricks firmware (see https://pybricks.com)
 - Motor for steering on port D (mandatory)
 - Motor 1 for driving on port A (mandatory)
 - Motor 2 for driving on port B (optional)
 - Motors used for driving cannot be angular (use Powered Up motors, not the ones from SPIKE Prime)
 
### Source
Based on the following excellent articles from Pybricks
 - https://pybricks.com/project/technic-42124-xbox/
 - https://pybricks.com/project/spike-hub-menu/
file: RC_technic_hub.py
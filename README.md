# ubuntu-stick v0.1
Navigate trough Ubuntu virtual desktops using a joystick

## Software setup

For python we need to have installed:
 - [pyautogui](http://pyautogui.readthedocs.io/en/latest/install.html) - send keyboard commans to OS
 - [serial](http://pyserial.readthedocs.io/en/latest/pyserial.html) read output of Arduino


 Also we will need a program to [control](http://manpages.ubuntu.com/manpages/xenial/man1/wmctrl.1.html) Ubuntu's window manager: `sudo apt-get install wmctrl`

! Important. You might need to change line 4 in the python file to reflect your setup:

 `ser = serial.Serial('/dev/ttyUSB0', 115200)`, set `/dev/ttyUSB0` to reflect Arduino location.

## Hardware

The arduino file assumes the use of an Arduino Uno board with a HC-S501 joystick control, connected as:

|Arduino   |HC-S501  |
|---|---|
|GND|GND|
|+5V|+5V|
|A0|VRx|
|A1|VRy|
|Digital2|SW|

To run the program launch the python script, after flashing the `arduino-HC-S501` to Arduino:

`python python-os-nav.py` or `python python-os-nav.py &` to run in background.

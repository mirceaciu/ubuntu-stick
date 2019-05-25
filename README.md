# ubuntu-stick v0.1

Navigate trough Ubuntu virtual desktops using a joystick.

Code is tested on Ubuntu 16 and Chrome browser.

Requires python3.


## Depedencies:

 - [pyautogui](http://pyautogui.readthedocs.io/en/latest/install.html) - send keyboard commans to OS
 - [serial](http://pyserial.readthedocs.io/en/latest/pyserial.html) read output of Arduino

Also we will need a program to [control](http://manpages.ubuntu.com/manpages/xenial/man1/wmctrl.1.html) Ubuntu's window manager: `sudo apt-get install wmctrl`

## Hardware

The arduino file assumes the use of an Arduino Uno board with a HW-504 joystick control, connected as:

|Arduino   |HC-S501  |
|---|---|
|GND|GND|
|+5V|+5V|
|A0|VRx|
|A1|VRy|
|Digital2|SW|

*Any arduino can be used as python will send the keyboard commands.

## Usage

1. Flash `arduino-HC-S501` to Arduino

2. Run python script: `python3 python-os-nav.py [options]` (might require `sudo`)

Possible options:

`--arduino <path/to/device>`

 - Specify location of arduino board.
 - Default: '/dev/ttyUSB0'
 - Short-hand: `-a`

`--debug <True/False>`

- Prints to console position when joystick is moved.
- Default: False
- Short-hand: `-d`

`--sticky <True/False>`

- When browser is selected up/down scrolls in page, left/right toggles tabs
- Default: False
- Short-hand: `-s`


## Tips:

 - to move out from scrolling inside the browser click the joystick
 - you can move the selected window to a new workspace by clicking and holding on the joystick while navigating to the workspace (move up/down/left/right)

## Todo list
 - update dependencies
 - build GUI or executable file
 - deal with sudo requirements
 

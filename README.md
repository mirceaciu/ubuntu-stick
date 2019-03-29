# ubuntu-stick v0.1

Navigate trough Ubuntu virtual desktops using a joystick.

Code is tested on Ubuntu 16 and Chrome browser.

Requires python3.

## Depedencies:

 - [pyautogui](http://pyautogui.readthedocs.io/en/latest/install.html) - send keyboard commans to OS
 - [serial](http://pyserial.readthedocs.io/en/latest/pyserial.html) read output of Arduino

Also we will need a program to [control](http://manpages.ubuntu.com/manpages/xenial/man1/wmctrl.1.html) Ubuntu's window manager: `sudo apt-get install wmctrl`

## Hardware

The arduino file assumes the use of an Arduino Uno board with a HC-S501 joystick control, connected as:

|Arduino   |HC-S501  |
|---|---|
|GND|GND|
|+5V|+5V|
|A0|VRx|
|A1|VRy|
|Digital2|SW|

## Usage

1. Flash `arduino-HC-S501` to Arduino

2. Run python script: `python3 python-os-nav.py [options]`

Possible options:

`--arduino <path/to/device>`

 - Specify location of arduino board.
 - Default: '/dev/ttyUSB0'
 - Short-hand: `-a`

`--debug <True/False>`

- Prints to console position when joystick is moved.
- Default: False
- Short-hand: `-d`

`--browserlock <True/False>`

- When browser is selected up/down scrolls in page, left/right toggles tabs
- Default: False
- Short-hand: `-b`

## Todo list
 - update dependencies
 - build GUI or executable file
 - deal with sudo requirements
 

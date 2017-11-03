import serial, pyautogui, time, os
import subprocess
import sys

# time.sleep(2)
joy_port = sys.argv[1]
debug = False

ser = serial.Serial('/dev/ttyUSB'+sys.argv[1], 115200)

def read_serial():
    val = ser.readline()
    val_s = val.split("|")
    return {"button": int(val_s[0]), "x": int(val_s[1]), "y": int(val_s[2])}

def active_window():
    output = ''
    pipe = subprocess.Popen(
        "wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/')",
        shell=True, stdout=subprocess.PIPE).stdout
    try:
        output = pipe.read()
    except:
        print 'meh'

    return output

def debounce(read_param, db_type, tresh):
    change_confidence = 0
    false_confidence = 0
    conf_level = 10

    if db_type == "<":
        for n in range(conf_level):
            if read_serial()[read_param] < tresh:
                change_confidence += 1
            else:
                false_confidence +=1

    elif db_type == ">":
        for n in range(conf_level):
            if read_serial()[read_param] > tresh:
                change_confidence += 1
            else:
                false_confidence +=1
    else:
        for n in range(conf_level):
            if read_serial()[read_param] == tresh:
                change_confidence += 1
            else:
                false_confidence +=1

    return change_confidence > false_confidence

while True:
    def_y = 506
    def_x = 498
    def_b = 1
    # print read_serial()

    if read_serial()["button"] == 0 and 'Google Chrome' in active_window():
        if debounce("button", "==", 0):
            os.popen('wmctrl -a Desktop')

    if read_serial()["x"] < 400 and read_serial()["button"] == 1:
        if debounce("x", '<', 400) and debounce("button", '==', 1):
            if debug: print 'x to left, confident'
            if 'Google Chrome' in active_window():
                pyautogui.hotkey('ctrl', 'shift', 'tab')
                time.sleep(0.2)
            else:
                pyautogui.hotkey('ctrl', 'alt', 'left')
        else:
            if debug: print 'x to left, FALSE'

    if read_serial()["x"] > 500 and read_serial()["button"] == 1:
        if debounce("x", '>', 500) and debounce("button", '==', 1):
            if debug: print 'x to right, confident'
            if 'Google Chrome' in active_window():
                pyautogui.hotkey('ctrl', 'tab')
                time.sleep(0.2)
            else:
                pyautogui.hotkey('ctrl', 'alt', 'right')
        else:
            if debug: print 'x to right, FALSE'

    if read_serial()["y"] < 400 and read_serial()["button"] == 1:
        if debounce("y", '<', 400) and debounce("button", '==', 1):
            if debug: print 'y to top, confident'
            if 'Google Chrome' in active_window():
                pyautogui.scroll(3)
            else:
                pyautogui.hotkey('ctrl', 'alt', 'up')
        else:
            if debug: print 'y to top, FALSE'

    if read_serial()["y"] > 600 and read_serial()["button"] == 1:
        if debounce("y", '>', 600) and debounce("button", '==', 1):
            if debug: print 'y to bottom, confident'
            if 'Google Chrome' in active_window():
                pyautogui.scroll(-3)
            else:
                pyautogui.hotkey('ctrl', 'alt', 'down')
        else:
            if debug: print 'y to bottom, FALSE'

    if read_serial()["y"] > 600 and read_serial()["button"] == 0:
        if debounce("y", '>', 600) and debounce("button", '==', 0):
            if debug: print 'y bottom and button, confident'
            pyautogui.hotkey('ctrl', 'alt', 'shift', 'down')
        else:
            if debug: print 'y bottom and button, false'

    if read_serial()["y"] < 400 and read_serial()["button"] == 0:
        if debounce("y", '<', 400) and debounce("button", '==', 0):
            if debug: print 'y top and button, confident'
            pyautogui.hotkey('ctrl', 'alt', 'shift', 'up')
        else:
            if debug: print 'y top and button, false'

    if read_serial()["x"] < 400 and read_serial()["button"] == 0:
        if debounce("x", '<', 400) and debounce("button", '==', 0):
            if debug: print 'x left and button, confident'
            pyautogui.hotkey('ctrl', 'alt', 'shift', 'left')
        else:
            if debug: print 'x left and button, false'

    if read_serial()["x"] > 500 and read_serial()["button"] == 0:
        if debounce("x", '>', 500) and debounce("button", '==', 0):
            if debug: print 'x right and button, confident'
            pyautogui.hotkey('ctrl', 'alt', 'shift', 'right')
        else:
            if debug: print 'x right and button, false'

import serial, pyautogui, time, os
import subprocess

ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    val = ser.readline()
    val_s = val.split("|")
    button = int(val_s[0])
    x = int(val_s[1])
    y = int(val_s[2])

    output = ''
    pipe = subprocess.Popen(
        "wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/')",
        shell=True, stdout=subprocess.PIPE).stdout
    try:
        output = pipe.read()
    except:
        pass

    if button == 0 and 'Google Chrome' in output:
        os.popen('wmctrl -a Desktop')

    if y > 600 and button == 1:
        output = ''
        pipe = subprocess.Popen(
            "wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/')",
            shell=True, stdout=subprocess.PIPE).stdout
        try:
            output = pipe.read()
        except:
            pass

        if 'Google Chrome' in output:
            pyautogui.scroll(-3)
        else:
            pyautogui.hotkey('ctrl', 'alt', 'down')

    if y < 400 and button == 1:
        output = ''
        pipe = subprocess.Popen(
            "wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/')",
            shell=True, stdout=subprocess.PIPE).stdout
        try:
            output = pipe.read()
        except:
            pass

        if 'Google Chrome' in output:
            pyautogui.scroll(3)
        else:
            pyautogui.hotkey('ctrl', 'alt', 'up')
    if x < 400 and button == 1:
        output = ''
        pipe = subprocess.Popen(
            "wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/')",
            shell=True, stdout=subprocess.PIPE).stdout
        try:
            output = pipe.read()
        except:
            pass

        if 'Google Chrome' in output:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            time.sleep(0.2)
        else:
            pyautogui.hotkey('ctrl', 'alt', 'left')

    if x > 500 and button == 1:
        output = ''
        pipe = subprocess.Popen(
            "wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/')",
            shell=True, stdout=subprocess.PIPE).stdout
        try:
            output = pipe.read()
        except:
            print 'meh'

        if 'Google Chrome' in output:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(0.2)
        else:
            pyautogui.hotkey('ctrl', 'alt', 'right')

    if y > 600 and button == 0:
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'down')
    if y < 400 and button == 0:
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'up')
    if x < 400 and button == 0:
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'left')
    if x > 500 and button == 0:
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'right')

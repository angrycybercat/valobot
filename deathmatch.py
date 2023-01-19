import pyautogui, keyboard, time, pyscreeze

pixel1 = pyautogui.Point(955,535)
pixel2 = pyautogui.Point(959,540)

pyautogui.FAILSAFE = False

def pixelchanged():
    color1 = pyautogui.pixel(955,535)
    color2 = pyautogui.pixel(959,540)
    return not(pyautogui.pixelMatchesColor(955,535,color1,tolerance=15)) or not(pyautogui.pixelMatchesColor(959,540,color2,tolerance=15))

def click():
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()

while True:
    while keyboard.is_pressed('3'):
        print('start in a while')
        time.sleep(0.5)
        while True:
            if pixelchanged():
                click()
                print('detected')
                break
            if keyboard.is_pressed('3'):
                print('program stopped')
                time.sleep(0.5)
                break
#

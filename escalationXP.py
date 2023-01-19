import pyautogui, time, keyboard, random, itertools, logging
from datetime import date

start_button = pyautogui.Point(431,761)
play_pos = pyautogui.Point(432,280)
escalation_pos = pyautogui.Point(507,313) #esc:594 ; dm:507
health_pos = pyautogui.Point(295,774)
playagain_button = pyautogui.Point(423,778)
skip_button = pyautogui.Point(880,323)

play_color = list(itertools.product(range(203,206),range(207,211),range(214,229)))+[(194, 196, 201),(194, 196, 200)]
health_color = (255,255,255)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('escalation.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

def printlog(string):
    t = time.localtime()
    current_time = str(time.strftime("%H:%M:%S", t))
    print('['+current_time+'] '+string)
    return logging.debug('['+current_time+'] '+string)

def OnMenu():
    if pyautogui.pixel(432,280) in play_color :
        printlog('On menu')
        return True
    else:
        return False

def OnRewardMenu():
    if pyautogui.pixel(329,324) == (234,238,178):
        printlog('On reward menu')
        return True
    return False

def click(coordinates):
    pyautogui.moveTo(coordinates)
    time.sleep(0.3)
    pyautogui.click()


def MoveMouse():
    pyautogui.moveRel(random.randint(-50,50), random.randint(-50,50), duration=1)

def Move():
    keyboard.press('a')
    time.sleep(0.5)
    keyboard.release('a')
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')    


def MatchStarted():
    while pyautogui.pixel(295,774) != health_color :
        continue
    printlog("Match Started")

def KeepAFK_MatchEnd():
    while True:
        time.sleep(random.randint(5,10))
        Move()
        if OnMenu():
            printlog("Match ended")
            break


printlog('\n')
print(date.today())
logging.debug(date.today())
count = 1
print("Program starting, 3sec to get ingame menu")
time.sleep(3)
om = 'On menu: '+str(OnMenu())
printlog(om)
if OnMenu():
    click(play_pos)
    time.sleep(1)
    click(escalation_pos)
    time.sleep(1.5)
    click(start_button)
time.sleep(1)
while True:
    MatchStarted()
    KeepAFK_MatchEnd()
    time.sleep(12)
    if OnRewardMenu():
        click(skip_button)
        time.sleep(2)  #we should check this
    click(playagain_button)
    time.sleep(0.5)
    click(playagain_button)
    count += 1
    printlog('Playing again for the {0}th time'.format(count))
    
#

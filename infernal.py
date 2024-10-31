import pyautogui
import pydirectinput
import time
from image_recognition import locateImage, clickImage, play, easy, deflation, expert, infernal, home, nextbtn, okbtn

def enterInfernal():
    # Click "play"
    playpos = 0
    while playpos == 0:   
        playpos = locateImage(play)
    time.sleep(1) # prevents early clicks on loops
    clickImage(playpos)
    # Scroll to second to last page (uses "expert button")
    expertpos = 0
    while expertpos == 0:
        expertpos = locateImage(expert)
    clickImage(expertpos)
     # Click map infernal
    infernalpos = 0
    while infernalpos == 0:
        infernalpos = locateImage(infernal) 
    clickImage(infernalpos)
    # Click "easy"
    easypos = 0
    while easypos == 0:
        easypos = locateImage(easy)
    clickImage(easypos)
    # Click "deflation"
    deflationpos = 0
    while deflationpos == 0:
        deflationpos = locateImage(deflation)
    clickImage(deflationpos)
    # Click "overwrite save"
    time.sleep(1) # sleep to make sure it appears on screen, does not delay program
    okpos = 0
    okpos = locateImage(okbtn)
    if okpos != 0:
        clickImage(okpos) 
    
def placeMonkeys():
    # Click "OK"
    okpos = 0
    while okpos == 0:
        okpos = locateImage(okbtn)
    clickImage(okpos)
    
    time.sleep(0.5) # Waits for box to disappear
    
    # Place sniper
    pyautogui.moveTo(1538, 507)
    pydirectinput.press('z')
    pyautogui.click(x=1538, y=507, clicks=2, interval=0.4)
    # Upgrade sniper 
    pyautogui.click(x=330, y=800, clicks=4, interval=0.1)
    pyautogui.click(x=330, y=650, clicks=2, interval=0.1)
    
    
    # Place Village
    pyautogui.moveTo(1575, 625)
    pydirectinput.press('k')
    pyautogui.click(x=1575, y=625, clicks=2, interval=0.1)
    # Upgrade Village
    pyautogui.click(x=330, y=500, clicks=2, interval=0.1)
    
    # Place alchemist 
    pyautogui.moveTo(1605, 499)
    pydirectinput.press('f')
    pyautogui.click(x=1605, y=499, clicks=2, interval=0.1)
    # Upgrade alchemist
    pyautogui.click(x=330, y=500, clicks=4, interval=0.1)
    pyautogui.click(x=330, y=800)
    
    # Place 2nd sniper, not required but speeds up process bc it pops lead bloons
    pyautogui.moveTo(106, 573)
    pydirectinput.press('z')
    pyautogui.click(x=106, y=573, clicks=2, interval=0.1)
    # Upgrade 2nd sniper
    pyautogui.click(x=1550, y=450)
    pyautogui.click(x=1550, y=600, clicks=3, interval=0.1)
    
    # Place hero, not required to beat map
    pyautogui.moveTo(837, 734)
    pydirectinput.press('u')
    pyautogui.click(x=837, y=734)
    
    # Start game
    pydirectinput.press('space', presses=2)
    
def goHome():
    # After winning
    nextpos = 0
    homepos = 0
    while nextpos == 0:
        nextpos = locateImage(nextbtn)
        if checkPixel((159, 906), (163, 81, 33)): # Checks for level up
            pyautogui.click(x=440, y=545)
        if checkPixel((902, 474), (144, 90, 210)): # Checks for level up
            pyautogui.click(x=440, y=545)
    clickImage(nextpos)
        
    while homepos == 0:
        homepos = locateImage(home)
    clickImage(homepos)

# legacy function, is now used to check for level up. 
def checkPixel(pos, color):
    screenshot = pyautogui.screenshot()
    pixel = screenshot.getpixel(pos)
    if pixel == color:
        return True
    else:
        return False



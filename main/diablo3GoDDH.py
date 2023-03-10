import pyautogui, time, os, logging, sys, random, copy, keyboard

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) #uncomment to block debug log messages

#Creation of constants assigned to the images in the folder
SEETHE = 'seethe'
PREPARATION = 'preparation'
FANOFKNIVES = 'fanofknives'
SMOKESCREEN = 'smokescreen'
NEWTRISTRAM = 'newtristram' #this picture automatically ends the macroing if needed
BOSSKILLED = 'bosskilled' #this picture should stop the auto clicking of numbers 1,2,3,4

#Coordinates of the buttons to press
GAME_REGION=(615, 980, 300, 100)
FINISHED = 'El programa ha lanzado los resultados' #La función para comenzar regresa este valor si es exitoso

def main():
    logging.debug('Program started, press ctrl-c to abort at any time')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    seethe = imPath('seethe.png')
    smokescreen = imPath('smokescreen.png')
    shadowpower = imPath('shadowpower.png')
    preparation = imPath('preparation.png')
    startPushing(seethe, smokescreen, shadowpower, preparation)

def toxico():
    pyautogui.press('enter')
    pyautogui.write('no digas mamadas, para eso mis compas', interval=0.25)
    pyautogui.press('enter')

def startPushing(seethe, smokescreen, shadowpower, preparation):
    while True:
        pyautogui.keyDown('space')
        pyautogui.mouseDown(button='left',duration=1)
        pyautogui.mouseUp(button='left')
        pyautogui.keyUp('space')
        if(pyautogui.locateOnScreen(seethe, region=(615,980,300,100)) is not None):
            pyautogui.press('4')
        if(pyautogui.locateOnScreen(smokescreen, region=(615,980,300,100)) is not None):
            pyautogui.press('3')
        if(pyautogui.locateOnScreen(shadowpower, region=(615,980,300,100)) is not None):
            pyautogui.press('2')
        if(pyautogui.locateOnScreen(preparation, region=(615,980,300,100)) is not None):
            pyautogui.press('1')
        if(keyboard.is_pressed('esc')):
            time.sleep(10)
        

def getGameRegion():
    """Obtains the region that the Diablo3 game is on the screen and assigns it to GAME_REGION. The game must be at the start screen (where the PLAY button is visible)."""
    global GAME_REGION
    logging.debug('Finding game region...')
    region = pyautogui.locateOnScreen(imPath('top_right_corner.png', confidence=0.7))
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')
    # calculate the region of the entire game
    topRightX = region[0] + region[2] # left + width
    topRightY = region[1] # top
    GAME_REGION = (topRightX - 1920, topRightY, 1920, 1080) # the game screen is always 640 x 480
    logging.debug('Game region found: %s' % (GAME_REGION,))

def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    return os.path.join('images', filename)


if __name__ == '__main__':
    main()
import pyautogui, time, os, logging, sys, random, copy

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
GAME_REGION=()
FINISHED = 'El programa ha lanzado los resultados' #La función para comenzar regresa este valor si es exitoso

def main():
    logging.debug('Program started, press ctrl-c to abort at any time')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    startPushing()

def toxico():
    pyautogui.press('enter')
    pyautogui.write('no digas mamadas, para eso mis compas', interval=0.25)
    pyautogui.press('enter')

def startPushing():
    while(pyautogui.locateOnScreen(imPath('top_right_corner.png', confidence=0.7)) is None):
        if(pyautogui.locateOnScreen(imPath('seethe.png', confidence=1)) is not None):
            pyautogui.press('4')
        if(pyautogui.locateOnScreen(imPath('smokescreen.png', confidence=1)) is not None):
            pyautogui.press('3')
        if(pyautogui.locateOnScreen(imPath('shadowpower.png', confidence=1)) is not None):
            pyautogui.press('2')
        if(pyautogui.locateOnScreen(imPath('preparation.png', confidence=1)) is not None):
            pyautogui.press('1')

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
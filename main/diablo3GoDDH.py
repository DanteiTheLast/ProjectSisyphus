import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages

#Creation of constants assigned to the images in the folder
SEETHE = 'seethe'
PREPARATION = 'preparation'
FANOFKNIVES = 'fanofknives'
SMOKESCREEN = 'smokescreen'

#Coordinates of the buttons to press
GAME_REGION=()
VENGEANCE_COORDINATES= None
SMOKESCREEN_COORDINATES= None
FANOFKNIVES_COORDINATES= None
PREPARATION_COORDINATES= None 

FINISHED = 'El programa ha lanzado los resultados' #La función para comenzar regresa este valor si es exitoso

def main():
    logging.debug('Program started, press ctrl-c to abort at any time')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    getGameRegion()

def startPushing():
    SEETHE

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

import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages

#Creation of constants assigned to the images in the folder
SEETHE = 'seethe'
GUNKAN_MAKI = 'gunkan_maki'
CALIFORNIA_ROLL = 'california_roll'
SALMON_ROLL = 'salmon_roll'
SHRIMP_SUSHI = 'shrimp_sushi'
UNAGI_ROLL = 'unagi_roll'
DRAGON_ROLL = 'dragon_roll'

#Coordinates of the buttons to press
VENGEANCE_COORDINATES= None
SMOKESCREEN_COORDINATES= None
FANOFKNIVES_COORDINATES= None
PREPARATION_COORDINATES= None 

FINISHED = 'El programa ha lanzado los resultados' #La función para comenzar regresa este valor si es exitoso

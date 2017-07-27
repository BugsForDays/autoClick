import argparse
import pyautogui
import time
import keyboard
import sys

programs = 'start, league, locate, circle'
parser = argparse.ArgumentParser()
parser.add_argument('program', help='Possible values: ' + programs)
args = parser.parse_args()

def windows_start_menu():
    pyautogui.click(x=31, y=1043)
def league():
    print('='*35)
    print('LEAGUE OF LEGENDS NO AFK CLICK BOT')
    print('='*35)
    input('Press ENTER, then switch to league and recall to continue.')
    for x in reversed(range(5)):
        print('Program starting in {0}. Press SPACE to terminate'.format(x), end='\r')
        time.sleep(1)
    while True:
        if keyboard.is_pressed('space'):
            print('League auto click program terminated')
            exit()
        else:
            pyautogui.click(x=766, y=642, button='right')
            time.sleep(1)
            pyautogui.click(x=1161, y=240, button='right')
            time.sleep(1)
def xy():
    print('='*30)
    print('POINTER LOCATER')
    print('='*30)
    print('CTRL + C to exit')
    while True:
        x, y = pyautogui.position()
        color = pyautogui.screenshot().getpixel((x,y))
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + ' RGB: ' + str(color)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
def click_the_circle():
    print('='*30)
    print('CLICK THE CIRCLE BOT')
    print('https://scratch.mit.edu/projects/30395368/')
    print('='*30)
    input('Press ENTER, then switch to the game to continue.')
    for x in reversed(range(5)):
        print('Program starting in {0}. Press SPACE to terminate'.format(x), end='\r')
        time.sleep(1)
    print('bot is running')
    while True:
        if keyboard.is_pressed('space'):
            print('Circle bot auto click program terminated')
            exit()
        else:
            center = pyautogui.locateCenterOnScreen('blue.png')
            # print(center)
            pyautogui.click(center)

if args.program == 'start':
    windows_start_menu()
elif args.program == 'league':
    league()
elif args.program == 'locate':
    xy()
elif args.program == 'circle':
    click_the_circle()
else:
    print('Invalid positional argument. Please try again.')

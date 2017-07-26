import argparse
import pyautogui
import time
import keyboard
import sys
programs = 'start, league'
parser = argparse.ArgumentParser()
parser.add_argument('program', help='Possible values: ' + programs)
args = parser.parse_args()

def windows_start_menu():
    pyautogui.click(x=31, y=1043)
def league():
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
if args.program == 'start':
    windows_start_menu()
elif args.program == 'league':
    league()
else:
    print('invalid argument')

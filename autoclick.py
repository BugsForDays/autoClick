import argparse
import pyautogui

programs = 'start '
parser = argparse.ArgumentParser()
parser.add_argument('program', help='Possible values: ' + programs)
args = parser.parse_args()

def windows_start_menu():
    pyautogui.click(x=31, y=1043)

if args.program == 'start':
    windows_start_menu()
else:
    print('invalid argument')

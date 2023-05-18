from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

amounts = True
maxAmount = 5    
line = 0

with open('twitchchat.txt') as f:
    lines = f.readlines()
    line = len(lines)

while True:
    sleep(1)
    lines = []
    with open('twitchchat.txt') as f:
        lines = f.readlines()
    
    while line < len(lines):
        print(lines[line])
        numbers = [int(s) for s in lines[line].split() if s.isdigit()]
        amount = 0.5 if not amounts or len(numbers) == 0 else numbers[0] if numbers[0] < maxAmount else maxAmount
        print(amount)
        if "left" in lines[line]:
            keyboard.press('a')
            sleep(0.5 if not amounts else amount)
            keyboard.release('a')
        elif "right" in lines[line]:
            keyboard.press('d')
            sleep(0.5 if not amounts else amount)
            keyboard.release('d')
        elif "jump" in lines[line]:
            keyboard.press(Key.space)
            sleep(0.5)
            keyboard.release(Key.space)
        elif "lump" in lines[line]:
            keyboard.press(Key.space)
            keyboard.press('a')
            sleep(0.5 if not amounts else amount)
            keyboard.release(Key.space)
            keyboard.release('a')
        elif "rump" in lines[line]:
            keyboard.press(Key.space)
            keyboard.press('d')
            sleep(0.5 if not amounts else amount)
            keyboard.release(Key.space)
            keyboard.release('d')
        elif "lash" in lines[line]:
            keyboard.press('a')
            sleep(0.01)
            keyboard.release('a')
            sleep(0.01)
            keyboard.press('a')
            sleep(0.01)
            keyboard.release('a')
        elif "rash" in lines[line]:
            keyboard.press('d')
            sleep(0.01)
            keyboard.release('d')
            sleep(0.01)
            keyboard.press('d')
            sleep(0.01)
            keyboard.release('d')
        elif "grapple" in lines[line]:
            keyboard.press('r')
            sleep(0.01)
            keyboard.release('r')
        line += 1
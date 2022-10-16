import pyautogui as pag


def click(mouse, time=0):
    if time == 0:
        if mouse == 0:
            pag.leftClick()
        elif mouse == 1:
            pag.rightClick()
    else:
        if mouse == 0:
            pag.mouseDown(button='left')
            delay(time)
            pag.mouseUp(button='left')
        elif mouse == 1:
            pag.mouseDown(button='right')
            delay(time)
            pag.mouseUp(button='right')
    delay(0.1)


def press(key, time=0):
    if time == 0:
        pag.press(key)
    else:
        pag.keyDown(key)
        delay(time)
        pag.keyUp(key)
    delay(0.1)


def write(string):
    pag.write(string)
    delay(0.1)


def delay(time):
    pag.time.sleep(time)

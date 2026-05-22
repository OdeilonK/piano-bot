import numpy as np
import pyautogui as pag
import mss
pag.PAUSE = 0
pag.FAILSAFE = False
with mss.MSS() as sct:

    monitor = {"top": 375, "left": 1038, "width": 226 , "height": 226}

    while True:
        img=np.array(sct.grab(monitor))
        for i in range(0,226,75):
            for k in range(0,226,75):
                if img[k,i][2] == 74:
                    pag.click(i+1038,k+375)

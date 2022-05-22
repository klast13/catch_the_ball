import cv2
import numpy as np
from PIL import ImageGrab
import pygetwindow

HEIGHT = 600


def get_screen():
    window = pygetwindow.getWindowsWithTitle('Catch the Ball')[0]
    # print(window.width, window.height)
    # размер окна 620 643 при 600x600
    img = ImageGrab.grab(bbox=(int(window.left + 10) + HEIGHT // 3,
                               int(window.top + 30),
                               int(window.left + window.width - 10) - HEIGHT // 3,
                               int(window.top + window.height - 10)))
    frame = np.array(img)
    # frame = cv2.cvtColor(src=np.array(img), code=cv2.COLOR_RGB2BGR)
    return frame
    # cv2.waitKey(10)
    # cv2.imshow('frame', frame)

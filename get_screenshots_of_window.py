import cv2
import numpy as np
from PIL import ImageGrab
import pygetwindow


def get_screen():
    while True:
        window = pygetwindow.getWindowsWithTitle('Catch the Ball')[0]
        print(window.left, window.top, window.width, window.height)
        img = ImageGrab.grab(bbox=(int(window.left),
                                   int(window.top),
                                   int(window.left + window.width),
                                   int(window.top + window.height)))
        frame = cv2.cvtColor(src=np.array(img), code=cv2.COLOR_RGB2BGR)
        #return frame
        cv2.waitKey(100)
        cv2.imshow('frame', frame)

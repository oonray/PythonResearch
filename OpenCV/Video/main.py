import cv2
import numpy as np
from mss import mss
from PIL import Image

mon = {'top': 10, 'left': 10, 'width': 1366, 'height': 768}

sct = mss()

writer = cv2.VideoWriter()

while True:
    img = np.array(sct.grab(mon))
    cv2.imshow('test', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

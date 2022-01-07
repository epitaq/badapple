import cv2
import numpy as np

def create (path):
    im = cv2.imread(path)
    im_g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh = 128
    im_bool = (im_g > thresh) * 1
    print(im_bool)
    cv2.imwrite('test2.png',im_bool)

if __name__ == "__main__":
    create('test1.jpg')
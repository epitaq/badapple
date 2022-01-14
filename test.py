import cv2
import numpy as np

def color (img):
    # for i in img:
    #     for i1 in i:
    #         su = int(str(i1[0]) + str(i1[1]) + str(i1[2]))
    #         #print(int(su/256))
    img.astype('uint8')
    im = img.tolist()
    print(np.shape(img))
    #cv2.imwrite('54-test.png', image)


if __name__ == '__main__':
    im =cv2.imread('54.png')
    color(im)
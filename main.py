import cv2
import numpy as np
import time

def scale_to_width(img, width):
    """幅が指定した値になるように、アスペクト比を固定して、リサイズする。
    """
    h, w = img.shape[:2]
    height = round(h * (width / w))
    dst = cv2.resize(img, dsize=(width, height))
    return dst

def create_pi (im, width):
    pixel = ['＊', '・']
    #im = cv2.imread(path)
    im_s = scale_to_width(im, width)
    im_g = cv2.cvtColor(im_s, cv2.COLOR_BGR2GRAY)
    #二値化
    # thresh = 128
    # im_bool = (im_g > thresh) * 1
    #im_bool = cv2.adaptiveThreshold(im_g, 1, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 0)
    ret, im_bool = cv2.threshold(im_g, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    for i in im_bool:
        for i1 in i:
            print(pixel[i1],end='')
        print()


def create_mv (path, width):
    cap = cv2.VideoCapture(path)
    sleep_time = (1000//(cap.get(cv2.CAP_PROP_FPS)))/1000
    #上書き表示用の定数
    ret, frame = cap.read()
    im_s = scale_to_width(frame, width)
    sz = np.shape(im_s)
    ow = '\033[' + str(sz[0]+1) + 'A'
    create_pi(frame, width)
    #2フレーム以降の表示
    while True:
        ret, frame = cap.read()
        if ret:
            print(ow)
            create_pi(frame, width)
            time.sleep(sleep_time)
        else:
            print()
            break



if __name__ == "__main__":
    width = 50
    create_mv('test.mp4', width)

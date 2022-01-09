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

def create_pi_2 (im, width):
    """
    BGR画像を入力し二値化した画像を出力
    """
    pixel = ['＊', '・']
    #im = cv2.imread(path)
    im_s = scale_to_width(im, width)
    im_g = cv2.cvtColor(im_s, cv2.COLOR_BGR2GRAY)
    #二値化
    ret, im_bool = cv2.threshold(im_g, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    for i in im_bool:
        for i1 in i:
            print(pixel[i1],end='')
        print()

def create_pi_gray (im, width):
    """
    BGR画像を入力し四つの記号に変換した画像を出力
    """
    pixel = ['＊','＋','・','　']
    #im = cv2.imread(path)
    im_s = scale_to_width(im, width)
    im_g = cv2.cvtColor(im_s, cv2.COLOR_BGR2GRAY)
    sh = np.shape(im_g)
    im_4 = [[0 for i in range(sh[1])] for i in range(sh[0])]
    #記号化
    a = 255 // (len(pixel)-1)
    for i in range(sh[0]):
        for i1 in range(sh[1]):
            im_4[i][i1] = im_g[i][i1] // a
    #出力
    for i in im_4:
        for i1 in i:
            print(pixel[i1],end='')
        print()
    #print(im_g)


def create_mv (path, width):
    #tim = []
    cap = cv2.VideoCapture(path)
    sleep_time_d = (1000//(cap.get(cv2.CAP_PROP_FPS)))/1000
    sleep_time = sleep_time_d
    #上書き表示用の定数
    ret, frame = cap.read()
    im_s = scale_to_width(frame, width)
    sz = np.shape(im_s)
    ow = '\033[' + str(sz[0]+1) + 'A'
    create_pi_gray(frame, width)
    #2フレーム以降の表示
    time0 = time.time()
    while True:
        time0 = time.time()
        ret, frame = cap.read()
        if ret:
            print(ow)
            create_pi_gray(frame, width)
            time1 = time.time()
            sleep_time = sleep_time_d - (time1 - time0)
            if sleep_time <= 0:
                sleep_time = 0
            #tim.append(sleep_time)
            time.sleep(sleep_time)
        else:
            print()
            break
    #print(tim)



if __name__ == "__main__":
    width = 20
    create_mv('/mnt/c/users/w17175/documents/work/badapple/badapple/test.mp4', width)
    # im = cv2.imread('test1.jpg')
    # im1 = create_pi_gray(im, width)
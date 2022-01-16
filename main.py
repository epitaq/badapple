from glob import escape
import cv2
import numpy as np
import time
import sys


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



def color8 (lst):
    h = 42.6
    id = int(16 + 36*(lst[2]//h) + 6*(lst[1]//h) + (lst[0]//h))
    out = '\033[38;5;' + str(id) + 'm'
    return out



def create_pi_gray (im, width):
    """
    BGR画像を入力し四つの記号に変換した画像を出力
    """
    pixel = ['＊','＋','・','　']
    #pixel = ['＠','井','＃','＊','＋','！','・','　'] #＠＃＄％＾＆＊（）＿｜？・￥>＜「」い
    #im = cv2.imread(path)
    im_s = scale_to_width(im, width)
    im_g = cv2.cvtColor(im_s, cv2.COLOR_BGR2GRAY)
    sh = np.shape(im_g)
    im_pi = [[0 for i in range(sh[1])] for i in range(sh[0])]
    #記号化
    a = 255 // (len(pixel)-1)
    for i in range(sh[0]):
        for i1 in range(sh[1]):
            im_pi[i][i1] = round(im_g[i][i1] / a)
    #出力
    for i in im_pi:
        for i1 in i:
            print(pixel[i1],end='')
            pass
        print()
    #print(im_pi)

def create_pi_color (im, width):
    """
    BGR画像を入力し四つの記号に変換し色をつけた画像を出力
    """
    #pixel = ['＊','＋','・','　']
    pixel = ['＃','＊']
    im_s = scale_to_width(im, width)
    im_g = cv2.cvtColor(im_s, cv2.COLOR_BGR2GRAY)
    sh = np.shape(im_g)
    #記号化 出力
    a = 255 // (len(pixel)-1)
    for i in range(sh[0]):
        for i1 in range(sh[1]):
            esc = color8(im_s[i][i1])
            num = round(im_g[i][i1] / a)
            print(esc, end='')
            print('\033[40m', end='')
            print('\033[1m', end='')
            print(pixel[num], end='')
        print('\033[0m')


def create_mv (path, width):
    tim = []
    cap = cv2.VideoCapture(path)
    sleep_time_d = (10000//(cap.get(cv2.CAP_PROP_FPS)))/10000
    sleep_time = sleep_time_d
    #上書き表示用の定数
    ret, frame = cap.read()
    im_s = scale_to_width(frame, width)
    sz = np.shape(im_s)
    ow = '\033[' + str(sz[0]+1) + 'A'
    create_pi_color(frame, width)
    #2フレーム以降の表示
    time0 = time.time()
    while True:
        time0 = time.time()
        ret, frame = cap.read()
        if ret:
            print(ow)
            create_pi_color(frame, width)
            time1 = time.time()
            sleep_time = sleep_time_d - (time1 - time0)
            if sleep_time >= 0:
                time.sleep(sleep_time)
            else:
                ret, frame = cap.read()
            
            tim.append(sleep_time)
            #tim.append(time1 - time0)
        else:
            print()
            break
    print(tim)



if __name__ == "__main__":
    if len(sys.argv) <= 1:
        width = 40
        mv = "badapple.mp4"
    else:
        mv = sys.argv[1]
        width = int(sys.argv[2])
    create_mv(mv, width)
    # im = cv2.imread('test1.jpg')
    # im1 = create_pi_gray(im, width)
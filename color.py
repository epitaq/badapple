# for i in range(0,8):
#     print('\033[3{}m'.format(i) + '{}'.format(i) ,end=(' '))

# for i in range(256):
#     print('\033[38;5;{}m'.format(i) + '{}'.format(hex(i)) ,end=' ')
# else:
#     print()

for r in range(1,255,50):
    for g in range(1,255,50):
        for b in range(1,255,50):
            h = 51
            id = int(16 + round(36*r/h) + round(6*g/h) + round(b/h))
            print('\033[38;5;{}m'.format(id) + '{}'.format(id) + '\033[0m' ,end=' ')
            print('({},{},{})'.format(r//h,g//h,b//h) ,end = ' ,')
            print()
            #print('\033[38;2;{};{};{}m'.format(r,g,b,) + hex(int(str(r)+str(g)+str(b))) )


# 0-  7:  standard colors (as in ESC [ 30–37 m)
# 8- 15:  high intensity colors (as in ESC [ 90–97 m)
# 16-231:  6 × 6 × 6 cube (216 colors): 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)
# 232-255:  grayscale from black to white in 24 steps
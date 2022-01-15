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
            id = 16 + 36*r//h + 6*g//h + b//h
            print('\033[38;5;{}m'.format(id) + '{}'.format(id) + '\033[0m' ,end=' ')
            print('({},{},{})'.format(r//h,g//h,b//h) ,end = ' ,')
            #print('\033[38;2;{};{};{}m'.format(r,g,b,) + hex(int(str(r)+str(g)+str(b))) )

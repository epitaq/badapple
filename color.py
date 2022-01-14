# for i in range(0,8):
#     print('\033[3{}m'.format(i) + '{}'.format(i) ,end=(' '))

for i in range(255):
    print('\033[38;5;{}m'.format(i) + '{}'.format(hex(i)) ,end=' ')
else:
    print()

for r in range(1,255,50):
    for g in range(1,255,50):
        for b in range(1,255,50):
            print('\033[38;2;{};{};{}m'.format(r,g,b,) + hex(int(str(r)+str(g)+str(b))) ,end='')

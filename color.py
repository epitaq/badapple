# for i in range(0,8):
#     print('\033[3{}m'.format(i) + '{}'.format(i) ,end=(' '))

for i in range(256):
    print('\033[38;5;{}m'.format(i) + '{}'.format(hex(i)) ,end=' ')
else:
    print()

for r in range(1,255,50):
    for g in range(1,255,50):
        for b in range(1,255,50):
            rgb = int(bin(r//32)[2:]+bin(g//32)[2:]+bin(b//64)[2:], 2)
            rbg = int(bin(r//32)[2:]+bin(b//64)[2:]+bin(g//32)[2:], 2)
            grb = int(bin(g//32)[2:]+bin(r//32)[2:]+bin(b//64)[2:], 2)
            gbr = int(bin(g//32)[2:]+bin(b//64)[2:]+bin(r//32)[2:], 2)
            bgr = int(bin(b//64)[2:]+bin(g//32)[2:]+bin(r//32)[2:], 2)
            brg = int(bin(b//64)[2:]+bin(r//32)[2:]+bin(g//32)[2:], 2)
            #print(bin(r//32)[2:]+bin(g//32)[2:]+bin(b//64)[2:])
            print('\033[38;5;{}m'.format(rgb) + 'test' + '\033[0m' ,end=' ')
            print('\033[38;5;{}m'.format(rbg) + 'test' + '\033[0m' ,end=' ')
            print('\033[38;5;{}m'.format(grb) + 'test' + '\033[0m' ,end=' ')
            print('\033[38;5;{}m'.format(gbr) + 'test' + '\033[0m' ,end=' ')
            print('\033[38;5;{}m'.format(bgr) + 'test' + '\033[0m' ,end=' ')
            print('\033[38;5;{}m'.format(brg) + 'test' + '\033[0m' ,end=' ')

            print('({},{},{})'.format(r,g,b) ,end = ' ')
            print('\033[38;2;{};{};{}m'.format(r,g,b,) + hex(int(str(r)+str(g)+str(b))) )

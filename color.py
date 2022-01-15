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
            id = 16 + 36*r + 6*g + b
            #print(bin(r//32)[2:]+bin(g//32)[2:]+bin(b//64)[2:])
            print('\033[38;5;{}m'.format(id) + '{}'.format(id) + '\033[0m' ,end=' ')
            print('({},{},{})'.format(r,g,b) ,end = ' ')
            print('\033[38;2;{};{};{}m'.format(r,g,b,) + hex(int(str(r)+str(g)+str(b))) )

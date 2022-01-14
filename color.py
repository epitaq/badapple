for i in range(0,8):
    print('\033[3{}m'.format(i) + '{}'.format(i) ,end=(' '))

for i in range(255):
    print('\033[38;5;{}m'.format(i) + '{}'.format(hex(i)) ,end=' ')

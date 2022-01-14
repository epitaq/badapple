for i in range(0,8):
    print('\033[3{}m'.format(i) + 'test' + '\033[0m')

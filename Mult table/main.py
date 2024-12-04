for i in range(1, 13):
    for item in range(1, 13):
        if len(str(i*item)) == 2:
            spaces = ' '
        elif len(str(i*item)) == 1:
            spaces = '  '
        else:
            spaces = ''
        print(i*item, spaces + "|", end='')
    print('')
    
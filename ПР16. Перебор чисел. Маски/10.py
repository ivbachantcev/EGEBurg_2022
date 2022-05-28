for i in '0123456789ABCDEF':
    for j in '0123456789ABCDEF':
        numb = int('1'+i+'DED'+j+'BABA', 16)
        if numb % int('BA', 16) == 0:
            print(numb, numb // int('BA', 16))
for i in range(10):
    for j in range(10):
        numb = int('12345'+ str(i) + '6' + str(j) + '8')
        if numb % 17 == 0:
            print(numb, numb // 17)
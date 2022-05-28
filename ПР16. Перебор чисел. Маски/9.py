for i in range(1245, 129945 + 1):
    numb = str(i)
    if numb[:2] == '12' and '45' in numb and i % 51 == 0:
        print(i, i // 51)

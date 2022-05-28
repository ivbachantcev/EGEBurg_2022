for i in '012':
    for j in '012':
        for k in '012':
            for m in '012':
                for z in '012':
                    # 2?1?2?1?2?1
                    numb = int('2'+i+'1'+j+'2'+k+'1'+m+'2'+z+'1', 3)
                    if numb % 148 == 0:
                        print(numb, numb // 148)
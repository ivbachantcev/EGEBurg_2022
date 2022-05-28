div = int('101101', 2)
for i in '01':
    for j in '01':
        for k in '01':
            for m in '01':
                for z in '01':
                    for y in '01':
                        numb = int('1'+i+'1'+j+'1'+k+'1'+m+'1'+z+y+'1', 2)
                        if numb % div == 0:
                            print(numb, div)

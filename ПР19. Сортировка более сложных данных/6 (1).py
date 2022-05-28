f = open('26-71.txt')
N, S= map(int, f.readline().split())
tovar={}
for i in range(N):
    cod, ves = map(int, f.readline().split())
    if cod in tovar:
        tovar[cod].append(ves)
    else:
        tovar[cod]=[ves]
        
for cod in tovar:
    tovar[cod].sort()

colvo=0
maxost=0
maxcod=0
for cod in tovar:
    vestov=0
    ost=0
    for i in range(len(tovar[cod])):
        if vestov + tovar[cod][i]<=S:
            vestov+=tovar[cod][i]
            ost += 1
            colvo+=1
    ost=len(tovar[cod]) - ost
    if ost>maxost:
        maxost=ost
        maxcod=cod
print(N-colvo, maxcod)

    
    

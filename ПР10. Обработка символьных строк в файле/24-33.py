# Автор: А.Н. Носкин

with open("k7c-1.txt") as Fin:
  s = Fin.readline()

k = 0
c1 = 'BCD'# строка проверки первого символа
c2 = 'BDE'# строка проверки второго символа
c3 = 'BCE'# строка проверки третьего символа
for i in range(len(s)-2):
    if s[i] in c1 and s[i+1] in c2 and s[i+2] in c3 \
       and s[i]!=s[i+1] and s[i+1]!=s[i+2]: # проверка повтора символов
      k += 1
print(k)
















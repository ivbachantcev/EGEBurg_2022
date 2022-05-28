with open('../файлы/10.txt') as f:
    s = f.readline()
count = 0
first = 'ADF'
second = 'CDF'
third = 'CDF'
for i in range(len(s) - 2):
    if s[i] in first and s[i+1] in second and s[i+2] in third and s[i] != s[i+2] and s[i+1] != s[i+2]:
        count += 1
print(count)

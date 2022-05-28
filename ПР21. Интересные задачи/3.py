a = int(input())
if 5 <= a % 10 <= 9 or a % 10 == 0 or 11 <= a % 100 <= 14:
    print(a, 'программистов')
elif 2 <= a % 10 <= 4:
    print(a, 'программиста')
else:
    print(a, 'программист')
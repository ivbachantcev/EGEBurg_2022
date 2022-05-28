f = open('26-77.txt')
N = int(f.readline())
marks = {}
pattern = {1, 2, 3, 4, 5, 6, 7, 8}
for i in range(N):
    year, type_mark = map(int, f.readline().split())
    if year in marks:
        marks[year].add(type_mark)
    else:
        marks[year] = {type_mark}
global_count = 0
max_year = 0
max_none_type = 0
for year in marks:
    none_type = len(pattern - marks[year])
    global_count += none_type
    if none_type > max_none_type:
        max_none_type = none_type
        max_year = year
    elif none_type == max_none_type:
        max_year = max(max_year, year)
print(global_count, max_year)
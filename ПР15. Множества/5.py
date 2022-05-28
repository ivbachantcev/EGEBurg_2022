def superset(s1, s2):
    if s1 == s2:
        print('Множества равны')
    elif s1 < s2:
        print(f'Объект {s2} является чистым супермножеством')
    elif s1 > s2:
        print(f'Объект {s1} является чистым супермножеством')
    else:
        print('Супермножества не обнаружены')


# тесты
set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}
superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)

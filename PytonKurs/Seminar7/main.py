

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))

# print(transformed_values == values)



#list_old = [2, 4, 7, 12]

## Вариант 1
##          что сделать              где взять          *при каком условии
#list_new = [(0 if num < 5 else num) for num in list_old if num > 5]

## Вариант 2
# for num in list_old:
#     list_new.append(0 if num < 5 else num)

## Вариант 3
# list_new = list(map(lambda num: 0 if num < 5 else num, list_old))

#print(list_new)


'''
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
'''
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

def find_farthest_orbit(orbits):
    s = [(dbl[0]*dbl[1] if dbl[0]!=dbl[1] else 0) for dbl in orbits]
    return orbits[s.index(max(s))]




orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits)) # 2.5 10

def same_by(func, vals):
    return len(set(map(func, vals))) in [0, 1]
                          
    




values = [0, 2, 10, 7]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
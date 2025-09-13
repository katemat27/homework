"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции 
    (функция ничего не возвращает)


def move_zeros(lst: list[float]) -> list:
    return lst
"""
move = [1, 0, 0, 2, 3, 0, 1]
def move_zeros(lst: list[float]) -> list:
    non_zeros = [x for x in lst if x!= 0]
    zeros = [x for x in lst if x== 0]
    return non_zeros + zeros

print(move_zeros(move))
print('Исходный список:', move)
#второй способ
move1 = [1, 0, 0, 2, 3, 0, 1]
def move_zeros_in(lst: list[float]) -> None:
    lst.sort(lambda x: x == 0)

    from copy import copy, deepcopy

    copy_lst = lst[:] # копирование списка copy_lst = copy(lst)
    lst.clear()
    zeros_count = 0
    for elem in copy_lst:
        if elem == 0:
            zeros_count += 1
        else:
            lst.append(elem)
    for i in range(zeros_count):
        lst.append(0)



    pos = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[pos] = lst[i]
            pos += 1
    for i in range(pos, len(lst)):
        lst[i] = 0

print('До:', move1)
move_zeros_in(move1)  
print('После:', move1)

#третий способ с filter
move2 = [1, 0, 0, 2, 3, 0, 1]
def m_z_f(lst: list[float])-> list:
    non_zeros = list(filter(lambda х: х != 0, lst))
    zeros = list(filter(lambda х: х == 0, lst))
    return non_zeros + zeros
print('До', move2)
print('После', m_z_f(move2))

#третий способ с sorted
move3 = [1, 0, 0, 2, 3, 0, 1]
def m_z_s(lst: list[float])-> list:
    return sorted(lst, key=lambda х: х== 0)
print('До', move3)
print('После', m_z_s(move3))
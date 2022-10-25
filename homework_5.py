# Задача 1. Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.

# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random as r

newlist = [r.randint(1, 10) for i in range(10)]

def moreThanFive():
    res_list = list(filter(lambda x: x > 5, newlist))
    print(f'List of numbers more than 5: \n{res_list}')

print(f'Original list: \n{newlist}')
moreThanFive()
print()

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
#  описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

N = [r.randint(1, 15) for i in range(20)]

def func(N):
    result = []
    r1 = r.randint(0, len(N)-1)
    min = N[r1]
    result.append(min)
    sliced_list = N[r1:]
    for i in range(0, len(sliced_list)):
        if sliced_list[i] > min:
            result.append(sliced_list[i])
            min = sliced_list[i]
    print(f'Random ascending sequence: \n{result}')

print(f'Original list: \n{N}')
func(N)
print()

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, 
# сколько всего совпадающих элементов есть в списке.
#  Удалите все повторяющиеся элементы.

# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 

# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

numbers = [r.randint(1, 10) for i in range(10)]

def get_unique_num(numbers):
    unique_num = []
    for number in numbers:
        if number not in unique_num:
            unique_num.append(number)
    print(f'List of unique elements: \n{unique_num}')

def count_dublicate():
    count = 0
    for number in numbers:
        if numbers.count(number) > 1:
            count += 1
    print(f'number of duplicated elemnts - {count}')

print(f'Original list: \n{numbers}')
get_unique_num(numbers)
count_dublicate()

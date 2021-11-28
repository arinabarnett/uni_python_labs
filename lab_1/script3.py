from numpy import random
from typing import List


# Отсортировать список произвольных чисел по возрастанию и убыванию

def get_random_numbers():
    return [random.randint(-100, 100) for _ in range(10)]


asc_nums = get_random_numbers()
desc_nums = get_random_numbers()

asc_sorted = sorted(asc_nums)
desc_sorted = sorted(desc_nums, reverse=True)

print('Произвольные числа:', asc_nums)
print('Отсортированный список произвольных чисел по возрастанию:', asc_sorted)
print('------------------------------------')
print('Произвольные числа:', desc_nums)
print('Отсортированный список произвольных чисел по убыванию:', desc_sorted)


# Без применения встроенных методов
def sort_ascending(arr: List[int]) -> List[int]:
    sorted_list = []
    while arr:
        minimum = arr[0]
        for i in arr:
            if i < minimum:
                minimum = i
        sorted_list.append(minimum)
        arr.remove(minimum)
    return sorted_list


def sort_descending(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] > arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


asc_nums_custom = get_random_numbers()
desc_nums_custom = get_random_numbers()

print('------------------------------------')
print('Произвольные числа:', asc_nums_custom)
print('Отсортированный список произвольных чисел по возрастанию:', sort_ascending(asc_nums_custom))
print('------------------------------------')
print('Произвольные числа:', desc_nums_custom)
print('Отсортированный список произвольных чисел по убыванию:', sort_descending(desc_nums_custom))

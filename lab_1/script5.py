# Создать пустой словарь
empty_dict = {}

print(empty_dict)

# Создать словарь, содержащий минимум три пары «ключ: значение»
person = {
    'name': 'Alice',
    'age': '23',
    'city': 'LA',
    'job': 'Actress'
}

print(person)


# Сгенерировать словарь, содержащий числа в роли ключей и квадраты чисел в роли значений.
def generate_dictionary():
    nums = {}
    for i in range(2, 11):
        nums[i] = i*i
    return nums


numbers = generate_dictionary()
print(numbers)

# Опробовать печать значения из словаря по ключу.
print(person['name'])
# Опробовать удаление элемента из словаря.
person.pop('age')
print(person)

# Опробовать методы словарей
nums_copy = numbers.copy()
print(person.get('job'))
print(nums_copy.keys())
print(nums_copy.values())

nums_copy.clear()
print(nums_copy)
print(person.popitem())

person.update({'nickname': 'Al'})
print(person)


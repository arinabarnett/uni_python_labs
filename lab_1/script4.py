# Опробовать методы списков

random_list = ['h', 'e', 'l', 'l', 'o']
another_list = ['w', 'o', 'r', 'l', 'd']

print(random_list.index('l'))
print(random_list.count('l'))
random_list.append(',')
random_list.extend(another_list)
random_list.insert(11, '!')
print(random_list)
random_list.remove('l')
random_list.pop(0)
random_list.reverse()
print(random_list)

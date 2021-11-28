from typing import List


# Cписок символов из текстовой строки
def get_list_of_letters(string: str) -> List[str]:
    arr = []
    for letter in string:
        arr.extend(letter)
    return arr


list_of_letters = get_list_of_letters('test')
print(list_of_letters)

# Пустой список
empty_list = []
print(empty_list)

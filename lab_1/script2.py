from typing import List


# Список символов строки, повторенных 2 раза
def get_repeated_letters_list(string: str) -> List[str]:
    arr = []
    for letter in string:
        arr.append(letter*2)
    return arr


list_of_letters = get_repeated_letters_list('spam')
print(list_of_letters)

import script0
import importlib

print("Hello, World")
print(2 ** 100)
print("A", "B")
print(("A", "B"))
print("C", end=" ")

print('Str1')
print("Str1 = 'test'")
print('Str1 = \'test\'\nStr2 = "pass"')

for item in [1, 2, 3]:
    print(item)

importlib.reload(script0)
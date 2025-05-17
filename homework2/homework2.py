
a = input("Введите число a: ")
b = input("Введите число b: ")

if not a.isdigit() or not b.isdigit():
    print("Ошибка: оба значения должны быть целыми числами.")
else:
    a = int(a)
    b = int(b)
    squares = [num ** 2 for num in range(a + 1, b) if num > 0]
    print("Список квадратов целых чисел между a и b:", squares)

import random

numbers = [random.randint(1, 100) for _ in range(10)]

print(f"Сгенерированный список: {numbers}")

print("Элементы, которые больше предыдущего элемента:")
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i])

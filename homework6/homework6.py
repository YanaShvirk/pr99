
import random

numbers = [random.randint(1, 100) for _ in range(10)]

print(f"Исходный список: {numbers}")

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(f"Список после замены минимального и максимального элементов: {numbers}")

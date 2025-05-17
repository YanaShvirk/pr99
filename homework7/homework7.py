import random
num_elements = random.randint(8, 15)
numbers = [random.randint(1, 100) for _ in range(num_elements)]
print(f"Исходный список: {numbers}")
numbers.insert(0, numbers.pop())
print(f"Список после циклического сдвига вправо: {numbers}")

numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input == 'end':
        break
    if not user_input.isdigit(): 
        print("Пожалуйста, введите допустимое число.")
        continue
    numbers.append(int(user_input))

print("Нечетные элементы списка:")
for num in numbers:
    if num % 2 != 0:
        print(num)

import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
user_numbers = []
for i, row in enumerate(ticket):
    user_input = int(input(f"Выберите число из строки {i+1} ({row}): "))
    if user_input in row:
        user_numbers.append(user_input)
    else:
        print(f"Число {user_input} не найдено в строке {i+1}. Попробуйте снова.")
        break

lottery_numbers = [random.choice(row) for row in ticket]
print(f"Ваши числа: {user_numbers}")
print(f"Числа лотереи: {lottery_numbers}")

matches = set(user_numbers).intersection(lottery_numbers)
print(f"Количество совпадений: {len(matches)}")

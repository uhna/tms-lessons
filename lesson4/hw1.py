# Вывести на экран числа кратные 5 от 0 до 100 включительн
# Сделать это с помощью функции range с шагом 5
# Сделать это с помощью функции range c шагом 1 и вложенным if

for i in range(0, 101, 5):
    print(i)

for a in range(0, 100, 1):
    if a % 5 == 0:
        print(f"Число {a} кратное 5")
    else:
        print(f"Число {a} не кратное 5")
# Пользователь вводит число. Вывести True если чётное, иначе - False.

input_number = input("Введите любое число: ")
if int(input_number) % 2 == 0:
    print("True")
else:
    print("False")
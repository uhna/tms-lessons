# Пользователь вводит год.
# Если введённый год високосный - выведите True, иначе - False.

year = int(input("Введите год: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("True")
else: print("False")
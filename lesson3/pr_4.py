# Пользователь вводит в консоль строку.
# Если выведенная строка является палиндромом - выведите True. Если не является - выведите False.

polindrom_1 = input("Введите палиндром: ")
polindrom_2 = polindrom_1[::-1]
if polindrom_1 == polindrom_2:
    print("True")
else: print("False")
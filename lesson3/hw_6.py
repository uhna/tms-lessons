# Пользователь вводит месяц и число. Выведите True, если такой день есть в году

input_month = input("Введите месяц: ")
input_day = int(input("Введите число месяца: "))

dict_month_day = {"январь": 31, "февраль": 28, "март": 31, "апрель": 30,
                  "май": 31, "июнь": 30, "июль": 31, "август": 31,
                  "сентябрь": 30, "октябрь": 31, "ноябрь": 30,
                  "декабрь": 31}

if input_month in dict_month_day and 1 <= input_day <= \
        dict_month_day[input_month]:
    print("True")
else:
    print("False")
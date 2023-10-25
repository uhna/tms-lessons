# Пользователь вводит название месяца на английском.
# Выведите количество дней в этом месяце (не учитывая високосный год).
# Подсказка: понадобится создать dict: название месяца -> количество дней.

input_month = input("Введите название месяца на английском: ")
dict_month_day = {"January": 31, "February": 28, "Mart": 31, "April": 30,
                  "May": 31, "June": 30, "July": 31, "August": 31,
                  "September": 30, "October": 31, "November": 30,
                  "December": 31}
day_month = dict_month_day.get(input_month)

print(f"Количество дней в веденном месяце: {day_month}")

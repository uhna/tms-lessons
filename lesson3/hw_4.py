# Пользователь вводит произвольную строку.
# Выведите кортеж из уникальных символов введённой строки.

input_rundom_str = input("Введите произвольную строку: ")
unique_symbols = tuple(set(input_rundom_str))

print(f"Кортеж из уникальных символов введенной вами строки: {unique_symbols}")
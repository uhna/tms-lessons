# Пользователь вводит в консоли число секунд.
# Выведите число секунд в виде:
# минуты:секунды.
# *дни:часы:минуты:секунды.

seconds_1 = input('Enter seconds: ')
min = int(seconds_1) // 60
second_1 = int(seconds_1) - min*60
print(f"{min}:{second_1}")

seconds_2 = input('Enter seconds: ')
# получаем целое количество дней
day = int(seconds_2) // 86400
# получаем целое количество часов
hour = (int(seconds_2) - day * 86400) // 3600
# получаем целое количество минут
min = (int(seconds_2) - hour * 3600) // 60
# получаем целое количество секунд
second_2 = (int(seconds_2) - hour * 3600) - min * 60

print(f"{day}:{hour}:{min}:{second_2}")



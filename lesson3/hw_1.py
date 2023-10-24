# Пользователь вводит одно число, сторона квардата.
# Вывести кортеж из трёх чисел: периметр квадрата, площадь квадрата, диагональ квадрата.
import math

input_square_side = input("Введите сторону квадрата: ")
perimeter_square = int(input_square_side) * 4
area_square = int(input_square_side) ** 2
diagonal_square = math.sqrt(int(input_square_side) ** 2 + int(input_square_side) ** 2)
taple = (perimeter_square, area_square, diagonal_square)
print(taple)
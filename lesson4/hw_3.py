# Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you"
# и продолжайте спрашивать до тех пор, пока ответ не будет корректным.

for i in range(0, 101, 1):
    print(i)
    answer = input("Should we break?: ")
    if answer == "yes":
        break
    if answer == "no":
        continue
    if answer != "yes" and answer != "no":
        print("Don't understand you")
        answer = input("Should we break?: ")

# Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.

#10. F(n<2) = 5; F(n) = (n-1)! - F(n-5)

import time
import matplotlib.pyplot as plt
from math import factorial
def recursive_f(n):         # рекурсивное решение
    if n < 2:
        return 5
    else:
        return (factorial(n-1)) - recursive_f(n-5)

def iterative_f(n):         # итерационное решение
    fn = [5] * (n + 1)
    f = 1
    for i in range(2, n):
        f *= i
    for i in range(5, n + 1):
        fn[i] = f + fn[i - 5]
    return fn[n]

try:
    print("Введите натуральное число n >= 1")
    n = int(input())
    while n < 1:  # ошибка в случае введения не натурального числа
        n = int(input("\nВы ввели число меньше 1"))

    k = 1

    if n > 30 and k != 0:
        k = int(input(
            "\nЧисло n > 30, вы хотите сделать сравнительную таблицу? Это может занять существенное время. (Да: 1 / Нет: 0):\n"))
    while k != 0 and k != 1:
        k = int(input("\nВы ввели не 1 и не 0. Введите 1, чтобы продолжить или 0, чтобы завершить программу:\n"))

    if k == 1:
        print("\nПрограмма формирует сравнительную таблицу и графики времени вычисления рекурсивным и итерационным подходом для n чисел, ожидайте...\n")

        recursive_times = []  # создание списков для дальнейшего построения таблицы
        recursive_values = []
        iterative_times = []
        iterative_values = []
        n_values = list(range(1, n + 1))

        for n in n_values:  # заполнение списков данными
            start = time.time()
            recursive_values.append(recursive_f(n))
            end = time.time()
            recursive_times.append(end - start)

            start = time.time()
            iterative_values.append(iterative_f(n))
            end = time.time()
            iterative_times.append(end - start)

        table_data = []  # создание и заполнение последующей таблицы
        for i, n in enumerate(n_values):
            table_data.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])

        print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)',
                                                         'Значение рекурсии', 'Значение итерации'))  # вывод таблицы
        print('-' * 105)
        for data in table_data:
            print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format(data[0], data[1], data[2], data[3], data[4]))


        plt.plot(n_values, recursive_times, label='Рекурсия')  # вывод графиков
        plt.plot(n_values, iterative_times, label='Итерация')
        plt.xlabel('n')
        plt.ylabel('Время (с)')
        plt.title('Сравнение рекурсивного и итерационного подхода')
        plt.legend()
        plt.show()

    print("\nРабота программы завершена.\n")

except ValueError:
    print("\nВы ввели число, не следуя условиям. Перезапустите программу и введите число, следуя инструкциям.")

except RecursionError:
    print("\nВы превысили относительную максимальную глубину рекурсии. Перезапустите программу и введите меньшее число, если хотите получать результат работы рекурсивного подхода и сравнительную таблицу.")


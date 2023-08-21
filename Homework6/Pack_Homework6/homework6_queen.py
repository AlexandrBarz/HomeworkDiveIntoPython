"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

import random

def is_queen_beat(position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True
    else:
        return False


def successful_position(count_successful):
    position = []
    n = 8
    count = 1
    count_iter = 0
    while count <= count_successful:
        count_iter += 1
        i = 0
        while i < n:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1

        if is_queen_beat(position):
            print(position, 'iter = ', count_iter)
            count += 1
        position.clear()


if __name__ == '__main__':
    print(is_queen_beat([[1, 1], [2, 7], [3, 5], [4, 8], [5, 2], [6, 4], [7, 6], [8, 3]]))
    print(is_queen_beat([[1, 2], [2, 4], [3, 6], [4, 8], [5, 1], [6, 3], [7, 5], [8, 7]]))
    successful_position(4)
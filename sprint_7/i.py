"""
I. Сложное поле с цветочками
Все языки	Python 3.7.3
Ограничение времени	1 секунда	2 секунды
Ограничение памяти	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Теперь черепашке Кондратине надо узнать не только, сколько цветочков она может собрать, но и как ей построить свой 
маршрут для этого. Помогите ей!

Напомним, что Кондратине надо дойти от левого нижнего до правого верхнего угла, а передвигаться она умеет только вверх 
и вправо.

Формат ввода
В первой строке даны размеры поля n и m (через пробел). Оба числа лежат в диапазоне от 1 до 1000. В следующих n строках 
задано поле. Каждая строка состоит из m символов 0 или 1 и завершается переводом строки. Если в клетке записана 
единица, то в ней растет цветочек.

Формат вывода
Выведите в первой строке максимальное количество цветочков, которое сможет собрать Кондратина. Во второй строке 
выведите маршрут в виде последовательности символов «U» и «R», где «U» означает передвижение вверх, а «R» – 
передвижение вправо.

Если возможных оптимальных путей несколько, то выведите любой.
"""

import sys


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    points = [[-1 for _ in range(m)] for _ in range(n)]
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j, s in enumerate(sys.stdin.readline().rstrip()):
            points[i][j] = int(s)

    dp[n - 1][0] = points[n - 1][0]

    for i in range(n - 1, -1, -1):
        for j in range(m):
            if i == n - 1:
                down_value = 0
            else:
                down_value = dp[i + 1][j]

            if j - 1 == -1:
                left_value = 0
            else:
                left_value = dp[i][j - 1]

            dp[i][j] = max(down_value, left_value) + points[i][j]

    print(dp[0][-1])
    
    route = []
    
    i = 0
    j = m - 1

    while not (i == n - 1 and j == 0):
        if i == n - 1:
            down_value = -1
        else:
            down_value = dp[i + 1][j]

        if j - 1 == -1:
            left_value = -1
        else:
            left_value = dp[i][j - 1]

        if down_value > left_value:
            route.append('U')
            i += 1
        else:
            route.append('R')
            j -= 1

    route.reverse()
    
    print(''.join(route))


if __name__ == '__main__':
    main()

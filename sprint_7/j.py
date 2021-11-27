"""
J. Путешествие
Все языки	Python 3.7.3
Ограничение времени	0.5 секунд	2.5 секунд
Ограничение памяти	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гоша решил отправиться в турне по островам Алгосского архипелага. Туристическая программа состоит из последовательного
посещения n достопримечательностей. У i-й достопримечательности есть свой рейтинг ri.

Впечатление от i-й достопримечательности равно её рейтингу ri. Гоша хочет, чтобы его впечатление от каждой новой
посещённой достопримечательности было сильнее, чем от предыдущей. Ради этого он даже готов пропустить некоторые места в
маршруте –— в случае, если они нарушают этот порядок плавного возрастания.

Помогите Гоше и найдите наибольшую возрастающую подпоследовательность в массиве рейтингов ri.

Формат ввода
В первой строке дано натуральное число n (1 ≤ n ≤ 3 ⋅ 103) –— сколько различных туристических мест есть в программе. Во
второй строке дано n натуральных чисел через пробел –— рейтинги этих достопримечательностей ri (1 ≤ ri ≤ 109).

Формат вывода
Сначала в отдельной строке выведите длину найденной подпоследовательности. В следующей строке выведите номера
достопримечательностей, которые образуют эту подпоследовательность.
"""

import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    r = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = [[[0] for i in range(n + 1)] for j in range(m + 1)]

if __name__ == '__main__':
    main()

# нужен паспортный стол и нужно прописаться в квартиру, Тихомирова нотариус
# 281270 Ольга Викторовна Тихомирова
# Соцработник
# сегодня до 15:30 завтра 9:30
# Крестовая 126 (Ярославна)
# ООО "Опека"

"""
A. Interactor
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Лена руководит разработкой тестирующей системы, в которой реализованы интерактивные задачи.
До заверщения очередной стадии проекта осталось написать модуль, определяющий итоговый вердикт системы для
интерактивной задачи. Итоговый вердикт определяется из кода завершения задачи, вердикта интерактора и вердикта
чекера по следующим правилам:

Вердикт чекера и вердикт интерактора — это целые числа от 0 до 7 включительно.
Код завершения задачи — это целое число от -128 до 127 включительно.
Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом,
и вердикту чекера в противном случае.
Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера.
Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом,
и 4 в противном случае.
Если интерактор выдал вердикт 6, итоговый вердикт равен 0.
Если интерактор выдал вердикт 7, итоговый вердикт равен 1.
В остальных случаях итоговый вердикт равен вердикту интерактора.
Ваша задача — реализовать этот модуль.

Формат ввода
Входной файл состоит из трёх строк. В первой задано целое число r (−128≤r≤127) — код завершения задачи, во второй —
целое число i (0≤i≤7) — вердикт интерактора, в третьей — целое число c (0≤c≤7) — вердикт чекера.
Формат вывода
Выведите одно целое число от 0 до 7 включительно — итоговый вердикт системы.
"""


import sys


def get_code(exit_code, interactor_code, checker_code):
    if interactor_code == 0:
        if exit_code == 0:
            return checker_code
        return 3

    if interactor_code == 1:
        return checker_code

    if interactor_code == 4:
        if exit_code == 0:
            return 4
        return 3

    if interactor_code == 6:
        return 0

    if interactor_code == 7:
        return 1

    return interactor_code


def main():
    exit_code = int(sys.stdin.readline().rstrip())
    interactor_code = int(sys.stdin.readline().rstrip())
    checker_code = int(sys.stdin.readline().rstrip())

    print(get_code(exit_code, interactor_code, checker_code))


if __name__ == '__main__':
    main()

"""
Задание связано с обратной польской нотацией. Она используется для парсинга арифметических выражений.
Еще её иногда называют постфиксной нотацией.

В постфиксной нотации операнды расположены перед знаками операций.

Пример 1:
3 4 +
означает 3 + 4 и равно 7

Пример 2:
12 5 /
Так как деление целочисленное, то в результате получим 2.

Пример 3:
10 2 4 * -
означает 10 - 2 * 4 и равно 2

Разберём последний пример подробнее:

Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию, которую этот знак обозначает,
то есть перемножить эти два числа. В результате получим 8.

После этого выражение приобретёт вид:

10 8 -

Операцию «минус» нужно применить к двум идущим перед ней числам, то есть 10 и 8. В итоге получаем 2.

Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек.

Для вычисления значения выражения, записанного в обратной польской нотации, нужно считывать выражение
слева направо и придерживаться следующих шагов:

Обработка входного символа:
Если на вход подан операнд, он помещается на вершину стека.
Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений, взятых из стека
в порядке добавления. Результат выполненной операции помещается на вершину стека.
Если входной набор символов обработан не полностью, перейти к шагу 1.
После полной обработки входного набора символов результат вычисления выражения находится в вершине стека.
Если в стеке осталось несколько чисел, то надо вывести только верхний элемент.
Замечание про отрицательные числа и деление: в этой задаче под делением понимается математическое целочисленное деление.
Это значит, что округление всегда происходит вниз. А именно: если a / b = c, то b ⋅ c — это наибольшее число, которое
не превосходит a и одновременно делится без остатка на b.

Например, -1 / 3 = -1. Будьте осторожны: в C++, Java и Go, например, деление чисел работает иначе.

В текущей задаче гарантируется, что деления на отрицательное число нет.

Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации. Числа и арифметические операции записаны
через пробел.

На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.

Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

Run ID: 52356315
"""

"""
Run ID: 52356315

-- ПРИНЦИП РАБОТЫ --
Происходит итерация по входной последовательности символов. 
Если символ является операндом, он добавляется в конец стека для временного хранения, 
в ином случае, из стека будут извлечены 2 последних элемента и для них будет выполнена 
функция соотвествующая действию оператора и результат выполнения будет добавлен в конец 
того же стека.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Стек предполагает, что чем раньше элемент в него вошёл, тем позве он их него выйдет (LIFO). 
Таким образом, сохраняются условия алгоритма польской нотации о порядке опрация над опреандами.
В моей реализации стек - это `list`. Гарантией сохранения свойств стека является использование 
метода `append` для добавления элементов и метода `pop` для извлечения элементов.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции добавления/извлечения из стека выполняются со сложностью O(1), 
поэтому из не надо учитывать в рассчёте, как и арифметические операции.
Остаётся только перебор всех элементов, поэтому сложность алгоритма будет составлять O(N).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Если последовательность содержит N элементов, то стек максимум может наполниться на 
(N * (2/3)) элементов, потому что на каждые 2 операдна дожен быть один оператор, а он в стек не попадает.
Поэтому мой алгоритм будет потреблять O(N * (2/3)) + O(N) = O(N) памяти.
"""

import sys
import operator


OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def calc_polish_notation(seq):
    stack = []
    for element in seq:
        if element in OPERATIONS:
            b, a = stack.pop(), stack.pop()
            stack.append(OPERATIONS[element](a, b))
        else:
            stack.append(int(element))

    return stack.pop()


def main():
    seq = sys.stdin.readline().rstrip().split()
    print(calc_polish_notation(seq))


if __name__ == '__main__':
    main()

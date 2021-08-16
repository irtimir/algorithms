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

"""
A. Лампочки
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого находятся лампочки. У каждой лампочки есть
своя яркость. Уровень яркости лампочки соответствует числу, расположенному в узле дерева. Помогите Гоше найти самую
яркую лампочку в гирлянде, то есть такую, у которой яркость наибольшая.
PIC

Формат ввода
На вход подается корень дерева.
Замечания про отправку решений
Выберите компилятор make. Решение нужно отправлять в виде файла с расширением, которое соответствует вашему языку
программирования. Если вы пишете на Java, имя файла должно быть Solution.java. Для остальных языков назовите файл
my_solution.ext, заменив ext на необходимое расширение.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.
Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(Node) -> int.

С++:
struct Node{
  int value;
  const Node* left = nullptr;
  const Node* right = nullptr;
};
int Solution(const Node* root);
Нужно подключить solution_tree.h

Go:
type Node struct {
value  int
left   *Node
right  *Node
}
Ваша функция должна иметь сигнатуру func Solution(*Node) int.

JS:
class CNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
Ваша функция должна иметь сигнатуру solution :: CNode -> Number.

Java:
Файл должен содержать public class Solution с функцией
public static int treeSolution(Node head)

class Node {
    int value;
    Node left;
    Node right;

    Node(int value) {
        this.value = value;
        right = null;
        left = null;
    }
}
Формат вывода
Функция должна вернуть максимальное значение яркости в узле дерева.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    current_max = root.value
    if root.left:
        max_l = solution(root.left)
        if max_l > current_max:
            current_max = max_l
    if root.right:
        max_r = solution(root.right)
        if max_r > current_max:
            current_max = max_r
    return current_max


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


def main():
    test()


if __name__ == '__main__':
    main()

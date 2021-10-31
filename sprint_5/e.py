"""
E. Дерево поиска
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гоша понял, что такое дерево поиска, и захотел написать функцию, которая определяет, является ли заданное дерево
деревом поиска. Значения в левом поддереве должны быть строго меньше, в правом —- строго больше значения в узле.
Помогите Гоше с реализацией этого алгоритма.
PIC

Формат ввода
На вход функции подается корень бинарного дерева.
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
Ваша функция должна иметь сигнатуру solution(root: Node) -> bool.

С++:
struct Node{
  int value;
  const Node* left = nullptr;
  const Node* right = nullptr;
};
bool Solution(const Node* root);
Нужно подключить solution_tree.h

Go:
type Node struct {
    value int
    left  *Node
    right *Node
}
Ваша функция должна иметь сигнатуру Solution(root *Node) bool.

JS:
class CNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
Ваша функция должна иметь сигнатуру solution :: CNode -> bool.

Java:
Файл должен содержать класс public class Solution с функцией
public static boolean treeSolution(Node head)

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
Функция должна вернуть True, если дерево является деревом поиска, иначе - False.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    current_value = root.value

    if root.left:
        if root.left.value >= current_value or not solution(root.left):
            return False

    if root.right:
        if root.right.value <= current_value or not solution(root.right):
            return False
    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 2
    assert not solution(node5)


def main():
    test()


if __name__ == '__main__':
    main()

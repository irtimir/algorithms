"""
B. Сбалансированное дерево
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть про сбалансированные деревья. Он решил написать функцию, которая определяет, сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое поддеревья каждой вершины отличаются по высоте не больше, чем на единицу.
PIC

Формат ввода
На вход функции подаётся корень бинарного дерева.
Замечания про отправку решений
Выберите компилятор make. Решение нужно отправлять в виде файла с расширением, которое соответствует вашему языку программирования. Если вы пишете на Java, имя файла должно быть Solution.java. Для остальных языков назовите файл my_solution.ext, заменив ext на необходимое расширение.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.
Python:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
Ваша функция должна иметь сигнатуру solution(Node root) -> bool.

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
Ваша функция должна иметь сигнатуру solution(root) :: CNode -> bool.

Java:
Файл должен содержать public class Solution с public static boolean treeSolution(Node head)

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
Функция должна вернуть True, если дерево сбалансировано в соответствии с критерием из условия, иначе - False.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def tree_height(root):
    if root.left is not None:
        left_height = tree_height(root.left)
    else:
        left_height = 0

    if root.right is not None:
        right_height = tree_height(root.right)
    else:
        right_height = 0

    if abs(right_height - left_height) > 1:
        raise ValueError()

    return 1 + max(left_height, right_height)


def solution(root):
    try:
        if root.left is not None:
            left_height = tree_height(root.left)
        else:
            left_height = 0

        if root.right is not None:
            right_height = tree_height(root.right)
        else:
            right_height = 0
        if abs(right_height - left_height) > 1:
            raise ValueError()
        return True
    except ValueError:
        return False


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node5 = Node(1)
    node6 = Node(-5)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


def main():
    test()


if __name__ == '__main__':
    main()

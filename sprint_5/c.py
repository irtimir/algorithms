"""
C. Дерево - анаграмма
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гоша и Алла играют в игру «Удивительные деревья». Помогите ребятам определить, является ли дерево, которое им
встретилось, деревом-анаграммой?
Дерево называется анаграммой, если оно симметрично относительно своего центра.
PIC

Формат ввода
Напишите функцию, которая определяет, является ли дерево анаграммой.
На вход подаётся корень дерева.
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
Файл должен содержать public class Solution с
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
Функция должна вернуть True если дерево является анаграммой. Иначе - False.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def compare_two(node1, node2):
    if bool(node1) == bool(node2):
        if not node1:
            return True
    else:
        return True

    if bool(node1.left) != bool(node2.left):
        return False
    if bool(node1.right) != bool(node2.right):
        return False

    return True


def solution(root):
    node1 = root.left
    node2 = root.right




def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)

"""
B. Удали узел
Ограничение времени	3 секунды
Ограничение памяти	128Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дано бинарное дерево поиска, в котором хранятся ключи. Ключи — уникальные целые числа. Найдите вершину с заданным
ключом и удалите её из дерева так, чтобы дерево осталось корректным бинарным деревом поиска. Если ключа в дереве нет,
то изменять дерево не надо.
На вход вашей функции подаётся корень дерева и ключ, который надо удалить. Функция должна вернуть корень изменённого
дерева. Сложность удаления узла должна составлять O(h), где h –— высота дерева.
Создавать новые вершины (вдруг очень захочется) нельзя.

Формат ввода
Ключи дерева – натуральные числа, не превышающие 109. В итоговом решении не надо определять свою структуру/свой класс,
описывающий вершину дерева.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.

Формат вывода
Выберите компилятор make. Решение нужно отправлять в виде файла с расширением, которое соответствует вашему языку
программирования. Если вы пишете на Java, имя файла должно быть Solution.java. Для остальных языков назовите файл
my_solution.ext, заменив ext на необходимое расширение. Ниже приведены сигнатуры функций, которые надо реализовать.
Python
# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left

def remove(root: Node, key: int) -> Node
C++

// do not declare Node in your submit-file
struct Node {
    Node∗ left;
    Node∗ right;
    int value;
};
#include "solution.h" // Attention!
Node∗ remove(Node∗ root, int key);
Java

// do not declare Node in your submit-file
public class Node {
    private Node left;
    private Node right;
    private int value;
    public int getValue();
    public Node getRight();
    public Node getLeft();
    public void setValue(int value);
    public void setRight(Node right);
    public void setLeft(Node left);
}
public class Solution {
        public static Node remove(Node root, int key);
}
Go

// do not declare Node in your submit-file
type Node struct {
        value    int
        left   ∗Node
        right  ∗Node
}

package main
func remove(node ∗Node, key int) ∗Node
NodeJs

// do not declare Node in your submit-file
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
function remove(node, key) {
    // your code
}
"""


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def unhook_last_right_vertex_from_left(root):
    parent_node = root
    current_node = parent_node.left

    if not current_node:
        return None

    if not current_node.right:
        return current_node

    while current_node.right:
        parent_node = current_node
        current_node = parent_node.right

    parent_node.right = current_node.left
    current_node.left = None
    return current_node


def unhook_last_left_vertex_from_right(root):
    parent_node = root
    current_node = parent_node.right

    if not current_node:
        return None

    if not current_node.left:
        return current_node

    while current_node.left:
        parent_node = current_node
        current_node = parent_node.left

    parent_node.left = current_node.right
    current_node.right = None
    return current_node


def remove(root, key):
    parent_node = None
    current_node = root

    while current_node:
        if key < current_node.value:
            parent_node = current_node
            current_node = parent_node.left
        elif key > current_node.value:
            parent_node = current_node
            current_node = parent_node.right
        else:
            if current_node.left:
                # finding the rightmost vertex in the left tree
                new_node = unhook_last_right_vertex_from_left(current_node)
                new_node.right = current_node.right
                if current_node.left is not new_node:
                    new_node.left = current_node.left
            elif current_node.right:
                # finding the leftmost vertex in the right tree
                new_node = unhook_last_left_vertex_from_right(current_node)
                new_node.left = current_node.left
                if current_node.right is not new_node:
                    new_node.right = current_node.right
            else:
                if parent_node:
                    # removing a leaf of a tree without children
                    if key < parent_node.value:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    break
                else:
                    # deleting the root of a tree without children
                    return None

            current_node.left = None
            current_node.right = None

            if parent_node:
                # connecting the parent node to the new node
                if parent_node.left is current_node:
                    parent_node.left = new_node
                else:
                    parent_node.right = new_node
                break
            else:
                # when removing a root, we get a new root
                return new_node

    return root


def test():
    # node1 = Node(None, None, 2)
    # node2 = Node(node1, None, 3)
    # node3 = Node(None, node2, 1)
    # node4 = Node(None, None, 6)
    # node5 = Node(node4, None, 8)
    # node6 = Node(node5, None, 10)
    # node7 = Node(node3, node6, 5)
    # newHead = remove(node7, 5)

    # print(newHead.left.right.value)

    # assert newHead.value == 5
    # assert newHead.right is node5
    # assert newHead.right.value == 8

    node10 = Node(None, None, 99)
    node9 = Node(None, None, 72)
    node8 = Node(node9, node10, 91)
    node7 = Node(None, None, 50)
    node6 = Node(None, None, 32)
    node5 = Node(None, node6, 29)
    node4 = Node(None, None, 11)
    node3 = Node(node7, node8, 65)
    node2 = Node(node4, node5, 20)
    node1 = Node(node2, node3, 41)

    head = remove(node1, 41)

    print(head.left.right.right.value)
    print(head.value)


def main():
    test()


if __name__ == '__main__':
    main()

"""
J. Добавь узел
Ограничение времени	3 секунды
Ограничение памяти	128Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дано BST. Надо вставить узел с заданным ключом. Ключи в дереве могут повторяться.
На вход функции подаётся корень корректного бинарного дерева поиска и ключ, который надо вставить в дерево. Осуществите вставку этого ключа. Если ключ уже есть в дереве, то его дубликаты уходят в правого сына. Таким образом вид дерева после вставки определяется однозначно. Функция должна вернуть корень дерева после вставки вершины.
Ваше решение должно работать за
O
(
h
)
, где
h
 –— высота дерева.
На рисунках ниже даны два примера вставки вершин в дерево.
PIC

Формат ввода
Ключи дерева – натуральные числа, не превосходящие
1
0
9
. Число вершин в дереве не превосходит
1
0
5
.
Замечания про отправку решений
Выберите компилятор make. Решение нужно отправлять в виде файла с расширением, которое соответствует вашему языку программирования. Если вы пишете на Java, имя файла должно быть Solution.java. Для остальных языков назовите файл my_solution.ext, заменив ext на необходимое расширение. Ниже приведены сигнатуры функций, которые надо реализовать.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.
Python
# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left

from node import Node # Attention!
def insert(root: Node, key: int) -> Node
C++

// do not declare Node in your submit-file
struct Node {
    Node∗ left;
    Node∗ right;
    int value;
};
#include "solution.h" // Attention!
Node∗ insert(Node∗ root, int key);
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
    public Node(Node left, Node right, int value);
}
public class Solution {
        public static Node insert(Node root, int key);
}
Go

// do not declare Node in your submit-file
type Node struct {
        value    int
        left   ∗Node
        right  ∗Node
}
package main

func insert(root ∗Node, key int) ∗Node
NodeJs

// do not declare Node in your submit-file
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
function insert(node, key) {
    // Your code
}
"""


# from node import Node

# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def insert(root, key):
    if key < root.value:
        if root.left is None:
            root.left = Node(None, None, key)
        else:
            insert(root.left, key)
    if key >= root.value:
        if root.right is None:
            root.right = Node(None, None, key)
        else:
            insert(root.right, key)
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


def main():
    test()


if __name__ == '__main__':
    main()

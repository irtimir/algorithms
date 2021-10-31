"""
K. Выведи диапазон
Ограничение времени	3 секунды
Ограничение памяти	128Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Напишите функцию, которая будет выводить по неубыванию все ключи от L до R включительно в заданном бинарном
дереве поиска.
Ключи в дереве могут повторяться. Решение должно иметь сложность
O(h+k), где h –— глубина дерева, k — число элементов в ответе.
В данной задаче если в узле содержится ключ x, то другие ключи, равные x, могут быть как в правом, так и в левом
поддереве данного узла. (Дерево строил стажёр, так что ничего страшного).
PIC

Формат ввода
На вход функции подаётся корень дерева и искомый ключ. Число вершин в дереве не превосходит 105. Ключи – натуральные
числа, не превосходящие 109. Гарантируется, что L≤R.
В итоговом решении не надо определять свою структуру / свой класс, описывающий вершину дерева.
Замечания про отправку решений
Выберите компилятор make. Решение нужно отправлять в виде файла с расширением, которое соответствует вашему языку
программирования. Если вы пишете на Java, имя файла должно быть Solution.java. Для остальных языков назовите файл
my_solution.ext, заменив ext на необходимое расширение.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.
Python
# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left
#################
def print_range(node: Node, l: int, r: int) -> pass
C++

// do not declare Node in your submit-file
struct Node {
    Node∗ left;
    Node∗ right;
    int value;
};
//
#include "solution.h" // Attention!
void print_range(Node∗ root, int L, int R);
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
//
public class Solution {
    public static void printRange(Node root, int L, int R, BufferedWriter writer) {
        // Your code
    }
}
Go

// do not declare Node in your submit-file
type Node struct {
        value    int
        left   ∗Node
        right  ∗Node
}
//
package main
func printRange(root ∗Node, left int, right int)
NodeJs

// do not declare Node in your submit-file
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
//
function printRange(root, left, right)
Формат вывода
Функция должна напечатать по неубыванию все ключи от L до R по одному в строке.
"""


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def print_range(node, l, r):
    if node.left and node.value >= l:
        print_range(node.left, l, r)

    if l <= node.value <= r:
        print(node.value)

    if node.right and node.value <= r:
        print_range(node.right, l, r)



def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8

def main():
    test()


if __name__ == '__main__':
    main()

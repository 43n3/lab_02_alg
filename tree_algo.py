# -----------------------------------------
# Бинарное дерево поиска (BST)
# -----------------------------------------

class BSTNode:
    """Узел бинарного дерева поиска."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """
    Бинарное дерево поиска.
    Методы: вставка, поиск, удаление узла.
    Сложность: O(log n) среднее, O(n) худший случай.
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставить значение в дерево. O(log n)"""
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)

    def find(self, value):
        """Найти значение в дереве. O(log n)"""
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def delete(self, value):
        """Удалить узел из дерева. O(log n)"""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def _min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        """Обход дерева in-order."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Вывести дерево в консоль."""
        if node is None and level == 0:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


# -----------------------------------------
# Сортировка кучей (Heap Sort)
# -----------------------------------------

def heapify(arr, n, i):
    """
    Восстановить Max-Heap для поддерева с корнем i.
    Сложность: O(log n)
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Сортировка кучей (Heap Sort).
    Сложность: O(n log n) во всех случаях.
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print(f"  Max-Heap построен: {arr}")

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        print(f"  Шаг: {arr}")

    return arr
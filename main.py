from graph_algo import Graph
from tree_algo import BST, heap_sort

# ============================================
# ЧАСТЬ 1: ГРАФ
# ============================================
print("=" * 50)
print("ЧАСТЬ 1: ГРАФ")
print("=" * 50)

vertices = [1, 2, 3, 4, 5, 6]
edges = [(1, 2), (2, 4), (4, 3), (3, 5), (5, 6)]

g = Graph(vertices)
for v1, v2 in edges:
    g.add_edge(v1, v2)

g.print_adjacency_matrix()
g.print_incidence_matrix()

print(f"\nDFS начиная с вершины 1: {g.dfs(1)}")
print(f"BFS начиная с вершины 1: {g.bfs(1)}")

components = g.find_connected_components()
print(f"\nКомпоненты связности: {components}")
print(f"Количество компонент: {len(components)}")

# ============================================
# ЧАСТЬ 2: БИНАРНОЕ ДЕРЕВО ПОИСКА
# ============================================
print("\n" + "=" * 50)
print("ЧАСТЬ 2: БИНАРНОЕ ДЕРЕВО ПОИСКА")
print("=" * 50)

values = [11, 6, 15, 3, 9, 13, 20]
tree = BST()
for v in values:
    tree.insert(v)

print("\nДерево после вставки всех элементов:")
tree.print_tree()

print(f"\nПоиск 13: {'Найден ✓' if tree.find(13) else 'Не найден ✗'}")

print("\nУдаление узла 6...")
tree.delete(6)
print("Дерево после удаления 6:")
tree.print_tree()
print(f"Обход in-order: {tree.inorder()}")

# ============================================
# ЧАСТЬ 3: HEAP SORT
# ============================================
print("\n" + "=" * 50)
print("ЧАСТЬ 3: HEAP SORT")
print("=" * 50)

arr = [11, 6, 15, 3, 9, 13, 20]
print(f"Исходный массив: {arr}")
sorted_arr = heap_sort(arr)
print(f"Отсортированный массив: {sorted_arr}")
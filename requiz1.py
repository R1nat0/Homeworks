"""
Реализовать работу с деревом поиска, где в качестве узла 
будет использоваться кортеж (value, left_child, right_child).
"""
start_tree = (2, (1, None, None), (3, None, None))

def add(tree: tuple, value: int) -> tuple:
    """
    На основе существующего дерева возвращает новое дерево с добавленным элементом.
    """
    if tree is None:
        return tuple((value, None, None))
    if value > tree[0]:
        return tuple((tree[0], tree[1], add(tree[2], value)))
    if value < tree[0]:
        return tuple((tree[0], add(tree[1], value), tree[2]))

def contains(tree: tuple, value: int) -> bool:
    """
    Возвращает true, если элемент есть в дереве.
    """
    if tree is None:
        return False
    if value > tree[0]:
        return contains(tree[2], value)
    if value < tree[0]:
        return contains(tree[1], value)
    return True


def tree_lenght(tree: tuple) -> tuple:
    """
    Возвращает глубину дерева.
    """
    if tree is None:
        return 0
    else:
        return 1 + max(tree_lenght(tree[1]), tree_lenght(tree[2]))

"""
 Используя методы из части А реализовать класс VersionedTree, 
 который будет инкапсулировать все версии дерева.
"""
class VersionedTree:
    def __init__(self, version=[None]):
        """
        Конструктор, создает объект и добавляет пустое дерево как версию 0.
        """
        self.version = version

    def add(self, value: int) -> None:
        """
        Создает новое дерево, добавив к последней версии элемент value,
        и добавляет его с инкрементированной версией.
        """
        self.version.append(add(self.version[-1], value))

    def contains(self, version: int, value: int) -> bool:
        """
        Возвращает true, если в версии version содержится элемент value.
        """
        return contains(self.version[version], value)

    def height(self, version: int) -> int:
        """
        Возвращает глубину дерева в версии version.
        """
        return tree_lenght(self.version[version])

if __name__ == "__main__":
    print(add(start_tree, 5))
    print(contains(start_tree, 2))
    print(tree_lenght(start_tree))

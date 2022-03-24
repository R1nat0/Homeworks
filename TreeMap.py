class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class TreeMap:
    def __init__(self, root):
        self.root = None
        self.size = 0

    def __setitem__(self, key, value):
        def inner_setitem(node):
            if node is None:
                return Node(key, value)
            else:
                if key == node.key:
                    node.value = value
                elif key < node.key:
                    node.left = inner_setitem(node.left)
                else:
                    node.right = inner_setitem(node.right)

                return node

    def __getitem__(self, key):
        def inner_getitem(node):
            if node is None:
                raise KeyError

            if key == node.key:
                return node.value

            elif key < node.key:
                return inner_getitem(node.left)
            else:
                return inner_getitem(node.right)

        return inner_getitem(self.root)

    @staticmethod
    def find_min_node(node):
        if node.left is not None:
            return TreeMap.find_min_node(node.left)
        return node

    def __delitem__(self, key):
        def inner_delitem(node, key):
            if node is None:
                raise KeyError

            if key < node.key:
                node.left = inner_delitem(node.left, key)
                return node
            elif key > node.key:
                result = inner_delitem(node.right, key)
                node.right = result
                return node

            else:

                if node.left is None and node.right is None:
                    return None
                elif node.left is not None and node.right is None:
                    return node.left
                elif node.left is None and node.right is not None:
                    return node.right
                else:
                    min_node = TreeMap.find_min_node(node.right)
                    node.key = min_node.key
                    node.value = min_node.value
                    node.right = inner_delitem(node.right, min_node.key)

                    return node
        self.root = inner_delitem(self.root, key)

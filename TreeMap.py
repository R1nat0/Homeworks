class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class TreeMap:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __setitem__(self, key, value):
        def add(node):
            if node is None:
                return Node(key, value)
            else:
                if key == node.key:
                    node.value = value
                elif key < node.key:
                    node.left = add(node.left)
                else:
                    node.right = add(node.right)

                return node

        self.root = add(self.root)
        self.size += 1

    def __getitem__(self, key):
        if self.root is None:
            raise KeyError
        else:
            node = self.get(key, self.root)
            if node is not None:
                return node.value
        raise KeyError

    def get(self, key, node):
        if key < node.key:
            return self.get(key, node.left)
        elif key > node.key:
            return self.get(key, node.right)
        elif node.key == key:
            return node
        else:
            return None

    @staticmethod
    def find_minn(node):
        if node.left is not None:
            return TreeMap.find_minn(node.left)
        return node

    def __delitem__(self, key):
        self.root = self.delete(self.root, key)

    def delete(self, node, key):
        if node is None:
            raise KeyError
        elif key > node.key:
            result = self.delete(node.right, key)
            node.right = result
            return node
        elif key < node.key:
            result = self.delete(node.left, key)
            node.left = result
            return node
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is not None and node.right is None:
                return node.left
            elif node.left is None and node.right is not None:
                return node.right
            else:
                minn = TreeMap.find_minn(node.right)
                node.key, node.value = minn.key, minn.value
                node.right = self.delete(node.right,    minn.key)
                return node

    def __iter__(self):
        if self.root is not None:
            yield from self.root

    def size(self):
        return self.size

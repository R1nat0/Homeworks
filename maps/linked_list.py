class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0

    def add(self, element):
        element = Node(element)
        if self.head is None:
            self.head = element
        else:
            self.end.next = element
        self.end = element
        self.length += 1

    def list_len(self):
        return self.length

    def out(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete(self, i):
        now = 1
        current = self.head
        self.length -= 1
        prenode = None
        while current is not None:
            if now == i:
                if prenode is not None:
                    prenode.next = current.next
                else:
                    self.head = current.next
                
            prenode = current
            current = current.next
            now += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next



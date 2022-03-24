from LinkedList import LinkedList

class HashMap:
    def __init__(self, size=2**3):
        self.size = size
        self.bucket = [LinkedList() for i in range(size)]
        self.length = 0

    def _get_hash(self, key):
            hash = 0
            for char in str(key):
                    hash += ord(char)
            return hash % self.size
    
    def __setitem__(self, key, value):
        hash = self._get_hash(key)
        for element in self.bucket[hash]:
            if key == element[0]:
                element[1] = value
                break
        else:
            self.bucket[hash].add([key, value])
            self.length += 1

        if self.length >= self.size * 0.8:
            self.size *= 2
            self.bucket = self.bucket + \
                [LinkedList() for i in range(self.size)]

    def __getitem__(self, key):
        hash = self._get_hash(key)
        for element in self.bucket[hash]:
            if element[0] == key:
                return element[1]
        raise KeyError

    def __str__(self):
        s = ''
        k = 0
        for i in range(self.size):
            for j in self.bucket[i]:
                s += str(j)
            s += '\n'
        return s

    def __delitem__(self, key):
        hash = self._get_hash(key)
        if self.bucket[hash] is not None:
            self.bucket[hash] = LinkedList()
            self.length -= 1

    def __len__(self):
        return self.length

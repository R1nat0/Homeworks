class Long:
    def __init__(self, number: int):
        self.number = number
        bucket = dict()
        i = 0
        for a in str(self.number):
            bucket[i] = int(a)
            i += 1   
        self.bucket = bucket
        self.length = len(str(number))
    
    def __add__(self, other):
        '''
        Не успел дореализовать
        '''
        if self.length >= other.length:
            res = self.bucket
            for i in range(other.length):
                res[i] = self.bucket[i] + other.bucket[i]
            return res
        else:
            res = other.bucket
            for i in range(self.length):
                res[i] = self.bucket[i] + other.bucket[i]
            return res

    def __sub__(self, other):
        '''
        Реализован неверно, я не успел
        '''
        res = dict()
        for i in range(self.length):
            res[i] = self.bucket[i] - other.bucket[i]
        return res 

    def __neg__(self):
        res = self.bucket
        res[0] = -(self.bucket[0])
        return res

    def __eq__(self, other):
        if self.length == other.length:
            for i in range(self.length):
                if self.bucket[i] == other.bucket[i]:
                    continue
                else: 
                    return False
            return True
        else: 
            return False

    def __ne__(self, other):
        if self.length == other.length:
            for i in range(self.length):
                if self.bucket[i] == other.bucket[i]:
                    continue
                else: 
                    return True
            return False
        else: 
            return True
    
    def __str__(self):
        return str(self.bucket)

    __repr__ = __str__

c = Long(125)
b = Long(233)
print(c)
print(b)
print(c + b)



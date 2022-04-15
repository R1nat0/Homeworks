import unittest
from  HashMap import HashMap
from LinkedList import LinkedList

class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hashmap = HashMap()

    def test_length(self):
        self.hashmap[0] = 1
        self.hashmap[1] = 'world'
        self.hashmap[7] = 43
        self.assertEqual(self.hashmap.length, 3)

    def test_len(self):
        self.hashmap[9] = 17
        self.assertEqual(len(self.hashmap), 1)

    def test_set_get(self):
        self.hashmap[0] = 13
        self.assertEqual(self.hashmap[0], 13)
        self.assertNotEqual(self.hashmap[0], 18)
    
    def test_delete(self):
        self.hashmap[0] = 56
        self.hashmap[5] = 13
        del(self.hashmap[5])
        self.assertEqual(len(self.hashmap), 1)
    
    def test_increase(self):
        self.hashmap[3] = 'Duck'
        self.hashmap['Kim'] = 54
        self.hashmap[1] = 'Cat'
        self.hashmap[8] = 74
        self.assertEqual(self.hashmap.size, 8)

if __name__ == '__main__':
    unittest.main()
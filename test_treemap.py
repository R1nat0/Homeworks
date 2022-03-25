import unittest
from TreeMap import TreeMap

class TestTreeMap(unittest.TestCase):
    def setUp(self):
        self.treemap = TreeMap()

    def test_root_none(self):
        self.assertEqual(self.treemap.root, None)

    def test_size(self):
        self.treemap[0] = 19
        self.treemap[1] = 45
        self.treemap[37] = 21
        self.assertEqual(self.treemap.size, 3)

    def test_get(self):
        self.treemap[0] = 125
        self.treemap[5] = 12
        self.assertEqual(self.treemap[5], 12)
        self.assertEqual(self.treemap[0], 125)

    def test_replace(self):
        self.treemap[15] = 12
        self.treemap[12] = 37
        self.treemap[15] = 59
        self.assertEqual(self.treemap[15], 59)

    def test_treevalue(self):
        self.treemap = TreeMap(8)
        self.assertNotEqual(self.treemap.root, None)
        self.assertEqual(self.treemap.root, 8)

if __name__ == '__main__':
    unittest.main()
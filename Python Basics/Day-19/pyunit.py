import unittest

def add(a, b):
    return a + b

class test(unittest.TestCase):
    def test_add_pos(self):
        self.assertEqual(add(5, 5), 10)

    def test_add_neg(self):
        self.assertEqual(add(-1, 1), 0)

    def text_add_mixed(self):
        self.assertEqual(add(-10, 5), 5)

unittest.main()
import unittest

class Test(unittest.TestCase):
    def testInstance(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b, "Fial")

    def testisInstance(self):
        a = [1, 2]
        self.assertIsInstance(a, list)

unittest.main()
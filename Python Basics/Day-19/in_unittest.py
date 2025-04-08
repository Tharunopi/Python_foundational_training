import unittest

class Test(unittest.TestCase):

    def testIn(self):
        self.assertIn(90, [1, 2, 3, 90])

    def testInN(self):
        self.assertIn(90, [1, 2, 3, 903])

unittest.main()
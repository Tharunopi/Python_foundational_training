import unittest

class Test(unittest.TestCase):

    def testStringUpper(self):
        self.assertTrue('S'.isupper())

    def testStringLower(self):
        self.assertFalse('S'.islower())

    def testStringPresence(self):
        self.assertIn("S", "SEQUEL")

    def testStringEquals(self):
        s1 = "cse it aids"
        self.assertEquals(s1.split(), ["cse", "it", "aids"])


unittest.main()
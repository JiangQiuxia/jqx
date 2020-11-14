import unittest
from count import Count

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def testAdd(self):
        a1 = Count(2,3)
        self.assertEqual(a1.add(),5)

    def testAdd2(self):
        a2 = Count(1,9)
        self.assertEqual(a2.add(),10)

if __name__ == '__main__':
    unittest.main()
import unittest
from count import Count

class TestSub(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def testSub(self):
        s1 = Count(1,2)
        self.assertEqual(s1.sub(),-1)

    def testSub2(self):
        s2 = Count(3,4)
        self.assertEqual(s2.sub(),-1)

if __name__ == '__main__':
    unittest.main()
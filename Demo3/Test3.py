import unittest
class Test3(unittest.TestCase):
    def setUp(self):
        print("test start")

    def testInclude(self):
        a="hello"
        b="hello world"
        self.assertIn(a,b,msg="a is not in b")

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()
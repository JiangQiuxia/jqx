from  Calculator import count
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

class TestCount(MyTest):

    def testAdd(self):
        j=count(2,3)
        self.assertEqual(j.add(),5)

    def testAdd2(self):
        j=count(1,9)
        self.assertEqual(j.add(),10)

    def testsub(self):
        s=count(2,3)
        self.assertEqual(s.sub(),-1)

    def testsub2(self):
        s=count(5,4)
        self.assertEqual(s.sub(),1)

    # def test3(self):
    #     m=count(1,2)
    #     self.assertTrue(m.isPrime(3),msg="Is not prime")



if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestCount("testAdd"))
    suite.addTest(TestCount("testAdd2"))
    suite.addTest(TestCount("testsub"))
    suite.addTest(TestCount("testsub2"))

    runner=unittest.TextTestRunner()
    runner.run(suite)
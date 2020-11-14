import unittest

class TestNumber(unittest.TestCase):

    def setUp(self):
        number = input("Enter a number：")
        self.number = int(number)

    def testNumber(self):
        self.assertEqual(self.number,10,msg="your input is not 10")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
import unittest

from Demo import Prime


class Test4(unittest.TestCase):
    def setUp(self):
        print("start")

    def testPrime(self):
        p=Prime()
        self.assertTrue(p.isPrime(7),msg="Is not prime")

    def tearDown(self):
        print("end")

if __name__ == '__main__':
    unittest.main()
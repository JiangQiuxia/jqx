import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test_aaa")

    @unittest.skipIf(3>2,"当条件为True时跳过测试")
    def test_skip_if(self):
        print("test_bbb")

    @unittest.skipUnless(3>2,"当条件为True时执行测试用例")
    def test_skip_unless(self):
        print("test_ccc")

    #不管结果是否失败，都统一标记为失败，但不会抛出错误信息
    @unittest.expectedFailure
    def test_skip_failure(self):
        print("test_ddd")

if __name__ == '__main__':
    unittest.main()
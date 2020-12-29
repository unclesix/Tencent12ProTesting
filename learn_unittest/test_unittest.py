import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

class Demo(unittest.TestCase):    #继承unittest.TestCase方法
    @classmethod
    def setUpClass(cls):        #setupclass 与 tearDownClass 作用域是整个类，先执行setupclass，然后再执行每一条测试用例，每一条测试用例之前之后又会执行setup 和 setdown。所有用例完成后执行teardownclas.
        print("setupclass")
    @classmethod
    def tearDownClass(cls):
        print("\nteardownclass")
    @classmethod
    def setUp(self):        #准备工作，自动调用
        print("setup")
    def tearDown(self):     #清理工作，自动调用
        print("tearDown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2,2,'判断相等')
        #self.assertNotIn('h','this')
        self.assertIn('h','this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1,1,'判断相等')
        #self.assertNotIn('h','this')
        self.assertIn('h','this')

    #@unittest.skip          #注解通过stkip方法调过test_case03用例
    @unittest.skipIf(1+1==2 ,"满足条件跳过test_case03")  #注解通过skioIf方法，如果满足条件则跳过test_case03用例
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3,2,'判断相等')
        #self.assertNotIn('h','this')
        #self.assertIn('h','this')

class Demo1(unittest.TestCase):    #继承unittest
    def test_demo1_case0(self):
        print("test_demo1_case0")
    def test_demo1_case1(self):
        print("test_demo1_case1")

class Demo2(unittest.TestCase):    #继承unittest
    def test_demo2_case0(self):
        print("test_demo2_case0")
    def test_demo2_case1(self):
        print("test_demo2_case1")


if __name__ == '__main__':
#执行方法一：
    #unittest.main()                 # unittest.main() 方法可以将模块中所有类下面的case执行
#执行方法二：加入容器执行
    # suite = unittest.TestSuite()
    # suite.addTest(Demo("test_case01"))
    # suite.addTest(Demo1("test_demo1_case0"))
    # unittest.TextTestRunner().run(suite)

#指定测试类运行
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo1)
    # suiteall = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suiteall)             #   OK (skipped=1)  test_case03跳过

#指定路径下所有的测试用例
    discover= unittest.defaultTestLoader.discover("./","test*.py")
    #unittest.TextTestRunner().run(discover)

    report_title = 'Example用例执行报告'
    desc = 'HTMLTestRunnerPY3'
    report_file = 'D:\\mylearntest\\learn_unittest\\UinttestExampleReport.html'

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)    #run.方法被HTMLTestRunnerPY3重写
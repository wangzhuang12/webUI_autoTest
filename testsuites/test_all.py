import unittest
import os
from testsuites.test_yongli1 import Test_yongli1
from testsuites.test_yongli2 import Test_yongli2
from testsuites.test_yongli3 import Test_yongli3
from testsuites.test_yongli4 import Test_yongli4
import HTMLTestRunner
import time


now = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
reporter_path = os.path.dirname(os.path.abspath('.'))+'/reporter/'
if not os.path.exists(reporter_path):os.mkdir(reporter_path)
#设置报告格式
reporter_name = reporter_path + now+ '_result.html'
fp =open(reporter_name,'wb')

suite =unittest.TestSuite()
# suite.addTest(unittest.makeSuite(BaseTestCase))
suite.addTest(unittest.makeSuite(Test_yongli1))
suite.addTest(unittest.makeSuite(Test_yongli2))
suite.addTest(unittest.makeSuite(Test_yongli3))
suite.addTest(unittest.makeSuite(Test_yongli4))
#suite=unittest.TestLoader.discover('./',pattern='test*.py')

if __name__ =="__main__":

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title='单元测试报告',description='用例执行情况')
    runner.run(suite)



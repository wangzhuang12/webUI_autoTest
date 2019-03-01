import unittest
from testsuites.base_testcase import BaseTestCase
import time
from pageobjects.home3_page import Home3Page



class Test_yongli3(BaseTestCase):

    def test_yongli3(self):

        #登录
        home3page = Home3Page(self.driver)
        home3page.login("wzz","123456")
        self.assertEqual(home3page.find_login(), "wzz", "failed to login")

        #搜索帖子
        home3page.search_card("魔都")
        self.assertEqual(home3page.find_search_result(), "魔都", "failed to login")

        #进入搜索帖子
        time.sleep(3)
        home3page.into_card()
        #判断
        home3page.decide()
        time.sleep(2)
        home3page.exit()
        time.sleep(2)
        self.assertEqual(home3page.find_exit(), "登录", "failed to login")


if __name__=='__main__':
    unittest.main()



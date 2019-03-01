import unittest
from testsuites.base_testcase import BaseTestCase
import time

from pageobjects.home_page import HomePage



class Test_yongli1(BaseTestCase):

    def test_yongli1(self):
        homepage = HomePage(self.driver)
        #登录
        homepage.login("wzz","123456")
        self.assertEqual(homepage.find_login(),"wzz","failed to login")


        #发表
        time.sleep(3)
        homepage.into_default()
        homepage.post_click()
        time.sleep(2)
        homepage.post("海贼王","sssssssssssssssss")
        time.sleep(15)
        self.assertEqual(homepage.find_subject(), "海贼王", "failed to post")

        #回复
        homepage.reply("111111111111111111111")
        time.sleep(3)
        self.assertEqual(homepage.find_reply(), "111111111111111111111", "failed to reply")

        #退出
        homepage.exit()
        time.sleep(3)
        self.assertEqual(homepage.find_exit(), "登录", "failed to login")


if __name__=='__main__':
    unittest.main()




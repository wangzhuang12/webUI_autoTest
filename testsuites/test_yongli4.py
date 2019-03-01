import unittest
from testsuites.base_testcase import BaseTestCase
import time
from pageobjects.home4_page import Home4Page

class Test_yongli4(BaseTestCase):

    def test_yongli4(self):
        # 登录
        home4page = Home4Page(self.driver)
        home4page.login("wzz", "123456")
        self.assertEqual(home4page.find_login(), "wzz", "failed to login")


        #发表投票贴.
        home4page.into_default()
        home4page.post_click()
        time.sleep(2)
        home4page.click_vote_post()
        time.sleep(2)
        home4page.vote("火影","卡卡西","六道斑","鼬","哈哈哈哈哈哈哈哈")
        time.sleep(3)
        self.assertEqual(home4page.find_subject(), "火影", "failed to login")


        # #进行投票
        home4page.option()
        home4page.take_out_option()

        self.assertEqual(home4page.find_leave_word(),"您已经投过票，谢谢您的参与","failed to vote")

        #主题名称
        home4page.take_out_subject()





if __name__=='__main__':
    unittest.main()



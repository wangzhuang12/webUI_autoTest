import unittest
from testsuites.base_testcase import BaseTestCase
import time
from pageobjects.home2_page import Home2Page




class Test_yongli2(BaseTestCase):

    def test_yongli2(self):

        home2page = Home2Page(self.driver)
        #登录
        home2page.login("admin", "123456")
        self.assertTrue(home2page.find_m_login().is_displayed())

        #进入默认板块
        home2page.into_default()
        #删除
        home2page.delete()
        #进入管理中心
        time.sleep(2)
        home2page.into_control()
        # home2page.logincontrol("123456")
        time.sleep(10)
        #进入论坛页面
        home2page.forum_link()
        #增加板块

        time.sleep(2)
        home2page.add_plate("默认板块")
        time.sleep(2)


        home2page.exit()
        #用户登录
        time.sleep(2)
        home2page.login("wzz","123456")
        self.assertEqual(home2page.find_login(),"wwz","failed to login.")
        #在新的板块发表
        home2page.post_new("死神","123456789123456789")
        self.assertEqual(home2page.find_subject(), "死神", "failed to post")
        #回复
        time.sleep(15)
        home2page.reply("hhhhhffffffff")


if __name__=='__main__':
    unittest.main()




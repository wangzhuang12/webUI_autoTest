from framework.base import BasePage
from selenium.webdriver.common.by import By

class Home2Page(BasePage):

    #登录
    username_page_input_search_loc = (By.NAME,'username')
    password_page_input_search_loc = (By.NAME,'password')
    login_page_click_search_loc = (By.CSS_SELECTOR,'.fastlg_l button')

    # 默认板块元素位置
    defaultSection_page_search_loc = (By.CSS_SELECTOR, '.fl_tb a')

    # 删除框的位置
    delete_box_page_loc = (By.CSS_SELECTOR, '#threadlisttableid tbody:nth-child(2) .o')
    delete_check_page_loc = (By.CSS_SELECTOR, '#mdly p:first-of-type strong:first-of-type a')
    sure_delete_page_loc = (By.CSS_SELECTOR, '#modsubmit')

    # 管理中心
    control_center_page_loc = (By.CSS_SELECTOR, '#um p:first-of-type a:nth-last-child(3)')

    #进入管理页面验证
    password1_page_input_search_loc = (By.CSS_SELECTOR, '.txt')
    login1_page_click_search_loc = (By.CSS_SELECTOR, '.btn')

    #论坛点击
    forum_page_loc = (By.CSS_SELECTOR, '#header_forum')


    #增加板块
    html_page_search_loc = (By.ID, 'main')
    plate_manage_page_loc = (By.CSS_SELECTOR,'.tabon')
    plate_page_loc = (By.CSS_SELECTOR,'.lastboard a')
    write_title_page_loc = (By.NAME,'newforum[1][]')
    submit_page_loc = (By.CSS_SELECTOR,'.fixsel input')

    # 退出位置
    exit_page_click_loc = (By.PARTIAL_LINK_TEXT, '退出')

    #进入新板块发帖
    new_plate_page_loc = (By.CSS_SELECTOR,'.fl_icn')
    post_title_page_loc =(By.ID,'subject')
    post_body_page_loc = (By.ID, 'fastpostmessage')
    post_button_page_loc = (By.ID,'fastpostsubmit')

    #回复
    reply_page_search_loc = (By.CSS_SELECTOR, '#post_reply img')
    reply_body_page_search_loc = (By.ID, 'postmessage')
    re_button_page_loc = (By.NAME, 'replysubmit')



    #断言
    manage_page_loc = (By.CSS_SELECTOR,'#g_upmine')
    new_plate1_page_loc = (By.CSS_SELECTOR,'.fl_tb a')
    #增加板块判断
    plate_number_page_loc = (By.CSS_SELECTOR,'#group_1 tr')
    #用户登录
    name_page_loc = (By.CSS_SELECTOR, '.vwmy')
    post_sucessful_page_loc = (By.CSS_SELECTOR, '#thread_subject')



    # 方法
    # 登录
    def login(self, name, password):
        self.sendkeys(name, *self.username_page_input_search_loc)
        self.sendkeys(password, *self.password_page_input_search_loc)
        self.click(*self.login_page_click_search_loc)

    # 点击默认板块
    def into_default(self):
            self.click(*self.defaultSection_page_search_loc)

    #删除帖子
    def delete(self):
        self.click(*self.delete_box_page_loc)
        self.click(*self.delete_check_page_loc)
        self.click(*self.sure_delete_page_loc)

    #点击管理中心
    def into_control(self):
        self.click(*self.control_center_page_loc)
        self.switch_window(self.window_handles()[1])
    #验证
    def logincontrol(self, password):
        self.switch_window(self.window_handles()[1])
        self.sendkeys(password, *self.password1_page_input_search_loc)
        self.click(*self.login1_page_click_search_loc)

    #论坛点击
    def forum_link(self):
        self.click(*self.forum_page_loc)

    #增加新版块
    def add_plate(self,title):

        main = self.current_window_handle()
        self.switch_iframe(*self.html_page_search_loc)
        self.click(*self.plate_page_loc)
        self.clear(*self.write_title_page_loc)
        self.sendkeys(title,*self.write_title_page_loc)
        self.click(*self.submit_page_loc)
        self.switch_window(main)
        self.close()

    #退出
    def exit(self):
        self.switch_window(self.window_handles()[0])
        self.click(*self.exit_page_click_loc)

    #快速发帖
    def post_new(self,p_title,p_body):

        # self.click(*self.new_plate_page_loc)
        self.switch_window(self.current_window_handle())
        self.sendkeys(p_title,*self.post_title_page_loc)
        self.sendkeys(p_body,*self.post_body_page_loc)
        self.click(*self.post_button_page_loc)


    #回复帖子
    def reply(self, content):
        self.click(*self.reply_page_search_loc)
        self.sendkeys(content, *self.reply_body_page_search_loc)
        self.click(*self.re_button_page_loc)


    #断言
    def find_m_login(self):
        a1 = self.find_element(*self.manage_page_loc)
        return a1


    def find_login(self):
        a3 = self.find_element(*self.name_page_loc)
        return a3.text
    def find_subject(self):
        a4 = self.find_element(*self.post_sucessful_page_loc)
        return a4.text


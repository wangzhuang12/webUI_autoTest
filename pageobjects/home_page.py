from framework.base import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    #登录
    username_page_input_search_loc = (By.NAME,'username')
    password_page_input_search_loc = (By.NAME,'password')
    login_page_click_search_loc = (By.CSS_SELECTOR,'.fastlg_l button')


    #默认板块元素位置
    defaultSection_page_search_loc = (By.CSS_SELECTOR,'#category_1 tbody tr:first-of-type td:nth-child(2) a')

    #发表元素位置
    post_page_search_loc = (By.CSS_SELECTOR,'#newspecial')

    #发表过程元素位置
    title_page_input_search_loc = (By.CSS_SELECTOR,'#subject')
    html_page_search_loc = (By.ID,'e_iframe')
    body_page_input_search_loc = (By.CSS_SELECTOR,'body')
    post_page_click_search_loc =(By.CSS_SELECTOR,'.mtm #postsubmit:first-of-type')

    #回复

    reply_page_search_loc = (By.CSS_SELECTOR,'#post_reply img')
    reply_body_page_search_loc =(By.ID,'postmessage')
    re_button_page_loc = (By.NAME,'replysubmit')


    #退出位置
    exit_page_click_loc = (By.PARTIAL_LINK_TEXT, '退出')


    #断言
    name_page_loc = (By.CSS_SELECTOR,'.vwmy')
    post_sucessful_page_loc = (By.CSS_SELECTOR,'#thread_subject')
    reply_sucessful_page_loc = (By.CSS_SELECTOR,'.t_f')






    #方法
    #登录
    def login(self, name, password):
        self.sendkeys(name, *self.username_page_input_search_loc)
        self.sendkeys(password, *self.password_page_input_search_loc)
        self.click(*self.login_page_click_search_loc)


    #点击默认板块
    def into_default(self):
        self.click(*self.defaultSection_page_search_loc)

    # 点击发表
    def post_click(self):
        self.click(*self.post_page_search_loc)

    #发表过程
    def post(self, title, body):
        self.sendkeys(title, *self.title_page_input_search_loc)
        main = self.current_window_handle()
        self.switch_iframe(*self.html_page_search_loc)
        self.sendkeys(body, *self.body_page_input_search_loc)
        self.switch_window(main)
        self.click(*self.post_page_click_search_loc)

    #回复操作
    def reply(self,content):
        self.click(*self.reply_page_search_loc)
        self.sendkeys(content,*self.reply_body_page_search_loc)
        self.click(*self.re_button_page_loc)

    #退出
    def exit(self):
        self.click(*self.exit_page_click_loc)


    #断言
    def find_login(self):
        a1 = self.find_element(*self.name_page_loc)
        return a1.text

    def find_subject(self):
        a2 = self.find_element(*self.post_sucessful_page_loc)
        return a2.text

    def find_reply(self):
        a3 =self.find_elements(*self.reply_sucessful_page_loc)
        return a3[-1].text

    def find_exit(self):
        a4 = self.find_element(*self.login_page_click_search_loc)
        return a4.text
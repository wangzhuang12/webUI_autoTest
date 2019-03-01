from framework.base import BasePage
from selenium.webdriver.common.by import By

class Home3Page(BasePage):
    # 登录
    username_page_input_search_loc = (By.NAME, 'username')
    password_page_input_search_loc = (By.NAME, 'password')
    login_page_click_search_loc = (By.CSS_SELECTOR, '.fastlg_l button')

    #搜索帖子
    search_input_page_loc = (By.CSS_SELECTOR,'#scbar_txt')
    search_button_page_loc = (By.CSS_SELECTOR,'#scbar_btn')

    #进入搜索帖子
    into_search_card_page_loc = (By.CSS_SELECTOR,'.xs3 font')

    # 判断是否符合期望
    card_title_page_loc = (By.CSS_SELECTOR,'#thread_subject')

    # 退出位置
    exit_page_click_loc = (By.PARTIAL_LINK_TEXT, '退出')


    #断言

    name_page_loc = (By.CSS_SELECTOR, '.vwmy')
    search_result_page_loc = (By.CSS_SELECTOR,'.xs3 font')




    # 方法
    # 登录
    def login(self, name, password):
        self.sendkeys(name, *self.username_page_input_search_loc)
        self.sendkeys(password, *self.password_page_input_search_loc)
        self.click(*self.login_page_click_search_loc)


    #搜索帖子：
    def search_card(self,content):
        self.click(*self.search_input_page_loc)
        self.sendkeys(content,*self.search_input_page_loc)
        self.click(*self.search_button_page_loc)
        self.switch_window(self.window_handles()[1])
    #进入搜索帖子
    def into_card(self):
        # self.switch_window(self.window_handles()[1])
        self.click(*self.into_search_card_page_loc)
        self.switch_window(self.window_handles()[2])

    #判断是否符合期望
    def decide(self):
        e1 = self.find_element(*self.card_title_page_loc).text
        if e1 =="魔都":
            print("正确")
        else:
            print("寻找不正确")

    # 退出
    def exit(self):
        self.switch_window(self.window_handles()[0])
        self.click(*self.exit_page_click_loc)


    #断言

    def find_login(self):
        a1 = self.find_element(*self.name_page_loc)
        return a1.text

    def find_search_result(self):
        a2 = self.find_element(*self.search_result_page_loc)
        return a2.text

    def find_exit(self):
        a4 = self.find_element(*self.login_page_click_search_loc)
        return a4.text
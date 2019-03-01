from framework.base import BasePage
from selenium.webdriver.common.by import By
import time

class Home4Page(BasePage):
    # 登录
    username_page_input_search_loc = (By.NAME, 'username')
    password_page_input_search_loc = (By.NAME, 'password')
    login_page_click_search_loc = (By.CSS_SELECTOR, '.fastlg_l button')

    #发表投票帖子(进入)
    defaultSection_page_search_loc = (By.CSS_SELECTOR, '#category_1 tbody tr:first-of-type td:nth-child(2) a')
    post_page_search_loc = (By.CSS_SELECTOR, '#newspecial')
    vote_page_search_loc = (By.CSS_SELECTOR,'#editorbox li:nth-child(2) a')
    #（标题选项输入）
    vote_title_page_loc = (By.ID,'subject')
    vote_option1_page_loc = (By.CSS_SELECTOR,'#pollm_c_1 p:first-of-type input')
    vote_option2_page_loc = (By.CSS_SELECTOR, '#pollm_c_1 p:nth-child(2) input')
    vote_option3_page_loc = (By.CSS_SELECTOR, '#pollm_c_1 p:nth-child(3) input')
    #(内容)
    html_page_search_loc = (By.ID, 'e_iframe')
    vote_body_page_loc = (By.CSS_SELECTOR,'body')
    post_vote_page_loc = (By.CSS_SELECTOR,'#postsubmit:first-of-type')


    #进行投票
    option_page_loc =(By.ID,'option_2')
    option_submit_page_loc = (By.CSS_SELECTOR,'#pollsubmit')

    #取内容
    option_titles_page_loc = (By.CSS_SELECTOR,'.pvt label')
    option_percent_page_loc = (By.CSS_SELECTOR,'.pcht tr td:nth-child(2)')

    #主题名称
    subject_page_loc = (By.CSS_SELECTOR,'#thread_subject')

    #断言
    name_page_loc = (By.CSS_SELECTOR, '.vwmy')
    post_sucessful_page_loc = (By.CSS_SELECTOR, '#thread_subject')
    leave_word_page_loc = (By.CSS_SELECTOR,'.pcht tr:nth-last-child(1) td')

    # 方法
    # 登录
    def login(self, name, password):
        self.sendkeys(name, *self.username_page_input_search_loc)
        self.sendkeys(password, *self.password_page_input_search_loc)
        self.click(*self.login_page_click_search_loc)

    #投票贴
    def into_default(self):
        self.click(*self.defaultSection_page_search_loc)

    def post_click(self):
        self.click(*self.post_page_search_loc)

    def click_vote_post(self):
        self.click(*self.vote_page_search_loc)

    def vote(self,votetitle,option1,option2,option3,body):

        #（输入）
        self.sendkeys(votetitle,*self.vote_title_page_loc)
        self.sendkeys(option1, *self.vote_option1_page_loc)
        self.sendkeys(option2, *self.vote_option2_page_loc)
        self.sendkeys(option3, *self.vote_option3_page_loc)
        #（内容）
        main = self.current_window_handle()
        self.switch_iframe(*self.html_page_search_loc)
        self.sendkeys(body, *self.vote_body_page_loc)
        self.switch_window(main)
        time.sleep(2)
        self.click(*self.post_vote_page_loc)

    #进行投票
    def option(self):
        self.click(*self.option_page_loc)
        self.click(*self.option_submit_page_loc)


    #取内容

    def take_out_option(self):
        e1 =self.find_elements(*self.option_titles_page_loc)
        for i in e1:
            # return i.text
            print(i.text)
        e2 = self.find_elements(*self.option_percent_page_loc)
        for j in e2:
            # return j.text
            print(j.text)

    #主题名称
    def take_out_subject(self):
        e3 = self.find_element(*self.subject_page_loc)
        return e3.text
        # print(e3.text)

    #断言
    def find_login(self):
        a1 = self.find_element(*self.name_page_loc)
        return a1.text

    def find_subject(self):
        a2 = self.find_element(*self.post_sucessful_page_loc)
        return a2.text

    def find_leave_word(self):
        a3 = self.find_element(*self.leave_word_page_loc)
        return a3.text
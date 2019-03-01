from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from framework.logger import Logger
import time
import os.path

logger = Logger(logger = "Basepage").getlog()

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.'))+ '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder :/screenshots")
        except Exception as e:
            logger.error("Failed to take screenshot! %s" % e)

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def open_url(self,url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quiting browser")
        except Exception as e:
            logger.error("Faild to quit the browser with %s" % e)


    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logger.error("找不到页面元素")
        self.get_windows_img()

    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            logger.error("找不到页面元素")
        self.get_windows_img()



    def sendkeys(self,text,*loc):
        e1 = self.find_element(*loc)
        # e1.clear()
        try:
            e1.send_keys(text)
            logger.info("输入内容"+text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
        self.get_windows_img()

    # def sendkey(self,text,*loc):
    #     e1 = self.find_element(*loc)
    #     # e1.clear()
    #     try:
    #         e1.send_keys(text)
    #         logger.info("输入内容"+text)
    #     except Exception as e:
    #         logger.error("Failed to type in input box with %s" % e)
    #     self.get_windows_img()

    def clear(self,*loc):
        e1 = self.find_element(*loc)
        try:
            e1.clear()
            logger.info("Clear text in input boxbefore typing.")
        except Exception as e:
            logger.error("Failed to clear in input box with %s" % e)
        self.get_windows_img()

    def click(self,*loc):
        e1 = self.find_element(*loc)
        try:
            e1.click()
            logger.info("The element %s was clicked ." % e1.text)
        except Exception as e:
            # logger.error("Failed to click th element with %s" % e)
            pass
    def switch_iframe(self,*loc):
        e1 =self.find_element(*loc)
        try:
            self.driver.switch_to.frame(e1)
            logger.info("switch main window")
        except Exception as e:
            logger.error("Failed to switch main window with %s" %e)

    def window_handles(self):
        try:
            e1 = self.driver.window_handles
            return e1
        except Exception as e:
            logger.error("Failed to return window handle for %s" % e )

    def current_window_handle(self):
        try:
            e1 = self.driver.current_window_handle
            return e1
            logger.info("找不到窗口")
        except Exception as e:
            logger.error("Failed ro return")


    def switch_window(self,*arg):
        try:
            self.driver.switch_to.window(*arg)
            logger.info("successful to switch .")
        except Exception as e:
            logger.error("Failed to awitch")


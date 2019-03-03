import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger = 'BrowserEngine').getlog()

class BrowserEngine(object):

    #获得浏览器路径
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir+'/tools/chromedriver.exe'
    # chrome_driver_path =  'D:/temp/pyth.project/Discuz/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firefox_driver_path = dir +'/tools/geckodriver.exe'


    #打开浏览器和网页
    def open_browser(self):
        config = ConfigParser()
        #读config文件
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        # file_path = 'D:/temp/pyth.project/Discuz/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("you had select %s browser" %browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is: %s" % url)


        if browser == "Firefox":
            driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("Start firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Start Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Start IE browser.")


        driver.get(url)
        logger.info("open url: % s" % url)
        driver.maximize_window()
        logger.info("Maximise the current window.")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds")
        return driver

    def quit_browser(self):
        self.driver.quit()




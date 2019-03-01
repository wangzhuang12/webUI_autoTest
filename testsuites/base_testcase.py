import unittest
from framework.browser_engine import BrowserEngine


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        open = BrowserEngine()
        self.driver=open.open_browser()


    def tearDown(self):

        self.driver.quit()




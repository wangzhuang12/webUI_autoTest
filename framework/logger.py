import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):

        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #设置文件名字，创建一个handler，用于写入文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name = log_path + rq + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # ch =logging.StreamHandler()
        # ch.setLevel(logging.INFO)


        #设置日志的格式

        formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        #把fh添加到handler里
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)



    def getlog(self):
        return self.logger



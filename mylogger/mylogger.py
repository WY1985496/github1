import logging

# 日志封装
class MyLogger:

    def __init__(self, level=logging.DEBUG):
        """创建日志器，设置日志器级别"""
        self.mylogger = logging.getLogger()
        self.mylogger.setLevel(level=level)


    def setFormat(self):
        """格式器，设置文件的输出格式"""
        self.contorl_format = logging.Formatter(fmt="%(asctime)s--> %(lineno)d行-->%(levelname)s-->%(message)s")
        self.file_format = logging.Formatter(fmt="%(filename)s ==》%(asctime)s ==》%(levelname)s ==》"
                                                    "%(lineno)d行 ==》%(message)s")
        return self.contorl_format, self.file_format


    def addControlHandler(self, level1=logging.WARNING):
        """设置控制台处理器，处理器设置级别，处理器添加格式器，日志器添加处理器"""
        self.control_handler = logging.StreamHandler()
        self.control_handler.setLevel(level=level1)
        self.control_handler.setFormatter(self.setFormat()[0])
        self.mylogger.addHandler(self.control_handler)


    def addFileHandler(self, file_name, level2=logging.INFO):
        """设置文件处理器，处理器设置级别，处理器添加格式器，日志器添加处理器"""
        self.file_handler = logging.FileHandler(filename=file_name, mode='a', encoding='utf-8')
        self.file_handler.setLevel(level=level2)
        self.file_handler.setFormatter(self.setFormat()[1])
        self.mylogger.addHandler(self.file_handler)

    def get_log(self,filename, Clevel=logging.INFO, Flevel=logging.INFO):
        """调用方法，并将日志器返回"""
        self.addControlHandler(level1=Clevel)
        self.addFileHandler(filename, level2=Flevel)
        return self.mylogger


# if __name__ == '__main__':
#     my_logger = MyLogger()
#     log = my_logger.get_log("test.log")
#     # 输出日志
#     log.critical('critical日志信息')
#     log.error('error日志信息')
#     log.warning('warning日志信息')
#     log.info('info日志信息')
#     log.debug('debug日志信息')

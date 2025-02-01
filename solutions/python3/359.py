
class Logger:

    # 构造函数，初始化日志字典
    def __init__(self):
        self.logs = {}

    # 检查是否应打印消息
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs or timestamp - self.logs[message] >= 10:
            # 如果消息不在日志中或时间戳与上次记录的时间差大于等于10，则更新日志并返回True
            self.logs[message] = timestamp
            return True
        else:
            # 否则返回False
            return False

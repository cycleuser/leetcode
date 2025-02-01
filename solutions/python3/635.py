
class LogSystem:

    def __init__(self):
        """
        初始化日志系统，存储时间戳和对应ID的列表。
        Initialize the log system with a list to store timestamps and corresponding IDs.
        """
        self.times = []
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id: str, timestamp: str):
        """
        添加一条记录，包含ID和对应的时间戳。
        Add a record with the given ID and timestamp.
        :param id: 记录的ID
        :param timestamp: 时间戳字符串
        """
        self.times.append([timestamp, id])

    def retrieve(self, s: str, e: str, gra: str):
        """
        根据给定的时间段和粒度检索记录。
        Retrieve records based on the given time range and granularity.
        :param s: 时间范围的起始时间戳
        :param e: 时间范围的结束时间戳
        :param gra: 粒度标识，可以是"Year", "Month", "Day", "Hour", "Minute", "Second"
        """
        ind = self.g[gra]
        s, e = s[:ind], e[:ind]  # 截取指定粒度的时间戳
        return [i for time, i in self.times if s <= time[:ind] <= e]  # 检索符合条件的记录

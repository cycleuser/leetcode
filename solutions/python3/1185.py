
from datetime import date

# Python 类定义示例，用于解决计算给定日期是星期几的问题
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """
        计算并返回给定日期是星期几
        :param day: 日期中的日份 (int)
        :param month: 日期中的月份 (int)
        :param year: 日期中的年份 (int)
        :return: 返回星期名称 (str)，例如 'Monday', 'Tuesday' 等
        """
        return date(year, month, day).strftime("%A")

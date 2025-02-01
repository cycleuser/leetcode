
class Solution:
    # 定义一个类，用于解析日期

    def dayOfYear(self, date: str) -> int:
        """
        计算给定日期在一年中的第几天
        
        参数：
            date (str): 格式为 'YYYY-MM-DD' 的字符串
        
        返回：
            int: 给定日期在一年中的天数
        """
        
        cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 定义一个列表，存储每个月的天数
        
        y, m, d = map(int, date.split('-'))
        # 将日期字符串按 '-' 分割，并转换为整数

        days = sum(cnt[:m - 1]) + d
        # 计算给定月份前的所有月份总天数加上当天的天数

        if m > 2:
            # 如果月份大于2月，需要考虑闰年情况
            
            if y % 400 == 0: 
                days += 1  # 闰年，2月有29天
            elif y % 100 == 0: 
                return days  # 能被100整除但不能被400整除的年份不是闰年
            elif y % 4 == 0: 
                days += 1  # 闰年，2月有29天

        return days

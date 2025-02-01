
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        定义一个类Solution，包含一个方法mincostTickets用于计算最小旅行成本。
        
        :param days: 一个整数列表，表示需要旅行的天数。
        :param costs: 一个整数列表，表示不同票种的价格。
        :return: 返回最小的成本。
        """
        day, days_set, last_day = [0] * 366, set(days), max(days)  # 初始化天数数组和集合，获取最后一天
        for i in range(1, last_day + 1):  # 遍历从1到last_day的每一天
            if i not in days_set:  # 如果当前不是需要旅行的日子
                day[i] = day[i - 1]  # 继承前一天的成本
            else:  # 否则，是需要旅行的一天
                # 计算三种不同票种下的最小成本，并更新当前day[i]
                day[i] = min(day[i - 1] + costs[0], 
                             day[max(0, i - 7)] + costs[1],  
                             day[max(0, i - 30)] + costs[2])
        return day[last_day]  # 返回最后一天的最小成本

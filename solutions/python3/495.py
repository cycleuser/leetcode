
class Solution:
    # 定义一个解决方案类

    def findPoisonedDuration(self, time_series, poison_duration):
        """
        :param time_series: 被毒药影响的时间序列，即每次中毒开始的时间点
        :type time_series: List[int]
        :param poison_duration: 每次中毒持续的时长
        :type poison_duration: int
        :return: 总共被毒药影响的总时间
        :rtype: int
        """
        
        # 将时间序列按顺序排序，方便计算重叠的时间段
        time_series.sort()
        
        result, upper_limit = 0, 0
        
        for idx, time in enumerate(time_series):
            # 如果当前时间段起始点大于上一个结束点，则更新上一个结束点为当前起始点
            if time > upper_limit:
                upper_limit = time
            
            # 计算当前时间段对总时长的贡献，并更新下一个时间段的结束点
            result, upper_limit = result + (time + poison_duration - upper_limit), time + poison_duration
        
        return result

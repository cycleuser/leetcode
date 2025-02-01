
class Solution:
    # 定义一个解决方案类

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        计算时间数组中可以配对且每对之和能被60整除的方案数。
        
        :param time: 时间列表，每个元素表示音乐播放时间（秒）
        :return: 返回能够配对的时间数量
        """
        mod = [0] * 61  # 创建一个长度为61的数组用于记录每种余数出现次数
        
        for t in time:
            # 对当前时间t取模60，找到其与某个元素组合能被60整除的匹配对个数
            mod[-1] += mod[(60 - t % 60) % 60]
            # 更新当前时间对应的计数字数
            mod[t % 60] += 1
        
        return mod[-1]  # 返回最后一项，即所有能够配对的方案总数

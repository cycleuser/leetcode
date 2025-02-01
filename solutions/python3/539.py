
class Solution:
    # 寻找时间数组中最小的时间差
    
    def findMinDifference(self, tp):
        # 将时间字符串转换为分钟数
        def getMinute(t): 
            h , m = t.split(":")
            return int(h) * 60 + int(m)
        
        # 对时间进行排序
        tp = sorted(map(getMinute, tp))
        
        mn = sys.maxsize  # 初始化最小时间差为一个很大的数
        
        # 遍历时间数组，找到最小的时间差
        for i in range(len(tp) - 1): 
            mn = min(mn, tp[i + 1] - tp[i])
            if mn == 0: return 0  # 如果找到了0分钟的间隔直接返回
        
        # 考虑跨午夜的情况
        return min(mn, 1440 + tp[0] - tp[-1])  # 返回最小的时间差，考虑跨越一天的情况

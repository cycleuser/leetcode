
class Solution:
    def minmaxGasDist(self, st, K):
        """
        初始化左右边界，寻找最小的最大间隔。
        
        中文注释：初始化左右边界，寻找最小的最大间隔。
        """
        left, right = 1e-6, st[-1] - st[0]
        # 使用二分查找法来逼近最小的最大间隔
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            """
            计算在给定的mid值下需要的最少分割次数，如果超过了K，则说明当前mid过小。
            
            中文注释：计算在给定的mid值下需要的最少分割次数，如果超过了K，则说明当前mid过小。
            """
            for a, b in zip(st, st[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > K:
                left = mid
            else:
                right = mid
        return right

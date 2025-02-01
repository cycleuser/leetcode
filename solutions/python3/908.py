
class Solution:
    # 定义一个方法smallestRangeI，接受两个参数A和K
    def smallestRangeI(self, A, K):
        # 计算最小值加上K
        l = min(A) + K
        # 计算最大值减去K
        r = max(A) - K
        
        # 如果最小值加上K大于等于最大值减去K，返回0
        if l >= r:
            return 0
        # 否则返回r-l的差值
        else:
            return r - l

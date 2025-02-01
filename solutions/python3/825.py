
from collections import Counter

class Solution:
    # 计算朋友请求的数量
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        
        # 使用Counter统计年龄出现次数
        cntr = Counter(ages)
        res = 0
        
        # 遍历每个年龄段A
        for A in cntr:
            # 遍历每个年龄段B
            for B in cntr:
                # 如果不符合请求条件则跳过本次循环
                if B <= 0.5 * A + 7 or B > A: continue
                
                # 当A和B相同时，计算组合数(A,B) = C(n,2)
                if A == B: res += cntr[A] * (cntr[A] - 1)
                # 当A不等于B时，直接计算两个年龄段的乘积
                else: res += cntr[A] * cntr[B]
        
        return res

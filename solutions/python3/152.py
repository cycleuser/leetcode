
class Solution:
    def maxProduct(self, nums):
        """
        使用动态规划的方法来解决最大乘积问题。
        
        Parameters:
        nums (List[int]): 输入的整数列表
        
        Returns:
        int: 最大乘积结果
        """
        res, min_pos, max_neg, cur = -float("inf"), float("inf"), -float("inf"), 1  # 初始化变量
        
        for num in nums:
            # 更新当前乘积值，并根据情况更新最大乘积结果
            cur *= num
            if cur > res: 
                res = cur
            elif 0 < cur // min_pos > res: 
                res = cur // min_pos
            elif 0 < cur // max_neg > res: 
                res = cur // max_neg
            
            # 处理当前乘积为0的情况，重置相关变量
            if cur == 0:
                min_pos, max_neg, cur = float("inf"), -float("inf"), 1
            elif max_neg < cur < 0:
                max_neg = cur
            elif 0 < cur < min_pos:
                min_pos = cur
        
        return res

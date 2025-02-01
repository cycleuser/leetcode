
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]  # 输入是一个整数列表
        :rtype: int           # 返回一个整数，表示按规则计算的和
        """
        nums.sort()            # 对输入列表进行排序
        
        sum = 0                # 初始化总和为0
        
        while nums:            # 当nums非空时循环
            num1 = nums.pop()  # 弹出最后一个元素作为num1
            num2 = nums.pop()  # 弹出倒数第二个元素作为num2
            
            sum += num2        # 将num2加到总和中
        
        return sum             # 返回最终的总和

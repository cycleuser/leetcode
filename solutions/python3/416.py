    
class Solution:
    def canPartition(self, nums):
        """
        判断给定的整数列表是否可以被分割成两个子集，使得两个子集的元素和相等。

        中文注释: 判断给定的整数列表是否可以被分割成两个子集，使得两个子集的元素和相等。
        """
        sm, n = sum(nums), len(nums)  # 计算总和并获取长度
        if sm % 2:  # 如果总和为奇数，则无法分割为两个等和子集
            return False
        
        sm //= 2  # 目标和为总和的一半

        dp = [False] * (sm + 1)  # 初始化动态规划数组
        dp[0] = True  # 空集合的和可以认为是0，所以初始化第一个值为True

        for num in nums:
            for j in range(num, sm + 1)[::-1]:  # 从大到小遍历dp数组
                dp[j] = dp[j] or dp[j - num]
        return dp[-1]  # 最后一个元素是否可以达到目标和
    
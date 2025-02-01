
class Solution:
    def pathSum(self, nums):
        """
        初始化动态规划表，用于存储路径和
        :param nums: List[int]
        :return: int
        """
        # 使用字典dp来存储每个节点的路径和
        dp = {(0, 1): 0}
        
        for num in nums:
            # 将数字转换为元组(d, p)
            d, p, v = map(int, str(num))
            
            # 更新当前节点的路径和
            dp[(d, p)] = v + dp[(d - 1, (p + 1) // 2)]
        
        # 计算符合条件的叶子节点的路径和总和
        return sum(dp[k] for k in dp if (k[0] + 1, k[1] * 2) not in dp and (k[0] + 1, k[1] * 2 - 1) not in dp)

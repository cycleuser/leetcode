
class Solution:

    # 动态规划计算最大抢劫金额
    def dp(self, nums):
        """
        使用动态规划求解子问题，跳过相邻的房屋进行抢劫。
        
        :param nums: List[int], 房屋中的金钱数数组
        :return: int, 最大抢劫金额
        """
        if len(nums) <= 2:
            # 如果房屋数量小于等于2，则直接返回最大值
            return max(nums or [0])
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            # 当前房屋的金钱数加上前两个或前三个房屋中较大的抢劫金额
            nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])

    # 主函数，根据实际情况选择最优方案
    def rob(self, nums):
        """
        根据房屋数量，决定是否从第一个或最后一个房屋开始进行抢劫。

        :param nums: List[int], 房屋中的金钱数数组
        :return: int, 最大抢劫金额
        """
        return max(self.dp(nums[:-1]), self.dp(nums[1:])) if len(nums) != 1 else nums[0]

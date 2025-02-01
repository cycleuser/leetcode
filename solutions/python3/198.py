
class Solution:
    # 定义一个类用于解决打家劫舍问题

    def rob(self, nums):
        """
        :param nums: List[int] - 一维数组，表示每户人家的金钱数
        :return: int - 最大能偷窃的金钱总数
        """
        if len(nums) <= 2:
            # 如果房子少于等于两栋，则直接返回最大值
            return max(nums or [0])

        nums[2] += nums[0]
        # 第三栋房子的钱加上第一栋，因为不能连续偷盗

        for i in range(3, len(nums)):
            # 从第三栋房子开始遍历到最后一栋
            nums[i] += max(nums[i - 2], nums[i - 3])
            # 对于当前房子i，可以选择不偷窃上一栋或上上一栋的最大值加上当前房子的钱

        return max(nums[-1], nums[-2])
        # 最后返回倒数第一和第二大的钱数中的较大者


class Solution:
    def findTargetSumWays(self, nums: list[int], S: int) -> int:
        """
        计算使数组中的所有数字加减之后等于目标和S的方案数。

        Args:
            nums (list[int]): 数组，包含整数。
            S (int): 目标和。

        Returns:
            int: 达到目标和S的方法总数。
        """
        d = {S: 1}  # 初始化字典，用于记录当前和为S的方案数量

        for i in range(len(nums)):  # 遍历数组
            new_d = collections.defaultdict(int)  # 创建一个新的默认值为0的字典来存储新的组合
            for k, v in d.items():  # 遍历字典d中的每个键值对
                new_d[k + nums[i]] += v  # 将当前和与nums[i]相加，计数累加到新字典中
                new_d[k - nums[i]] += v  # 将当前和与nums[i]相减，计数累加到新字典中
            d = new_d  # 更新d为新的组合字典

        return d[0]  # 返回结果字典中和为0的方案数量

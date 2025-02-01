
class Solution:
    # 定义一个类来解决寻找数组中第一个缺失的正整数的问题

    def firstMissingPositive(self, nums: List[int], res: int = 1) -> int:
        # 初始化结果变量，用于记录最小缺失正整数，默认值为1
        for num in sorted(nums):
            # 遍历排序后的数组，检查当前数字是否等于结果变量
            res += num == res
            # 如果相等，则结果变量不变；否则增加结果变量的值
        return res
        # 返回最终的结果变量，即最小缺失正整数

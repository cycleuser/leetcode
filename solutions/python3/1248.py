
class Solution:
    # 定义一个方法，计算数组中满足条件的子数组数量
    def numberOfSubarrays(self, nums: List[int], k: int, cnt: int = 0) -> int:
        # 构建奇数索引列表，包括哨兵元素-1和len(nums)
        odds = [-1] + [i for i, num in enumerate(nums) if num % 2 == 1] + [len(nums)]
        
        # 计算符合条件的子数组数量
        return sum(
            (odds[j - k + 1] - odds[j - k]) * (odds[j + 1] - odds[j])
            for j in range(k, len(odds) - 1)
        )

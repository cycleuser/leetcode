
class Solution:
    # 定义组合总和问题的解决方案类

    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 用于存储子问题的结果以避免重复计算
        memo = {}
        
        # 深度优先搜索函数，用于递归求解目标值为目标的组合个数
        def dfs(sm):
            # 如果当前状态已计算过，则直接返回结果
            if sm in memo:
                return memo[sm]
            else:
                # 当剩余和大于等于目标时，判断是否完全匹配
                if sm >= target:
                    memo[sm] = 1 if sm == target else 0
                    return memo[sm]
                cnt = 0
                # 遍历每个数字，递归计算子问题的结果并累加到当前计数中
                for num in nums:
                    memo[sm + num] = dfs(sm + num)
                    cnt += memo[sm + num]
                return cnt
        # 从和为0开始进行搜索
        return dfs(0)

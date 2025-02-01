
class Solution:
    def maxCoins(self, nums):
        # 初始化备忘录和扩充后的数组
        memo, nums = {}, [1] + [num for num in nums if num] + [1]

        def dfs(l, r):
            # 基线条件：只有两个元素时，无需爆破气球
            if r - l == 1:
                return 0

            # 如果该子问题未被解决，则尝试所有可能的中间点进行计算，并记录结果到备忘录中
            if (l, r) not in memo:
                memo[(l, r)] = max(nums[l] * nums[i] * nums[r] + dfs(l, i) + dfs(i, r)
                                  for i in range(l + 1, r))

            # 返回子问题的解
            return memo[(l, r)]

        # 调用深度优先搜索从第一个气球到最后一个气球爆破的所有可能情况
        return dfs(0, len(nums) - 1)

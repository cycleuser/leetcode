
class Solution:
    # 定义一个解决方案类

    def largestDivisibleSubset(self, nums):
        # 初始化dp列表，其中每个元素为该数字的单元素子集
        # 通过排序确保后续的遍历可以正确判断是否可被整除
        dp = [[num] for num in sorted(nums)]
        n = len(nums)

        # 双重循环遍历所有可能的组合
        for i in range(n - 1):
            for j in range(i + 1, n):
                # 检查dp[j]中的最后一个元素是否能被dp[i]中的最后一个元素整除
                if not dp[j][-1] % dp[i][-1] and len(dp[i]) >= len(dp[j]):
                    # 更新dp[j]
                    dp[j] = dp[i] + [dp[j][-1]]

        # 返回最长的可被整除子集，注意可能为空的情况
        return sorted(dp, key=len)[-1] if dp else []

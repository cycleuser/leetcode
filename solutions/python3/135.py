
class Solution:
    # 定义一个求解糖果分配问题的类

    def candy(self, ratings):
        # 初始化动态规划数组，每个孩子至少得到一颗糖
        dp = [1] * len(ratings)

        # 从前向后遍历rating列表
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                # 如果当前孩子的rating比前一个高，则分配的糖果数为前一个孩子的糖果数+1
                dp[i] = dp[i - 1] + 1

        # 从后向前遍历rating列表
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and dp[i] <= dp[i + 1]:
                # 如果当前孩子的rating比下一个孩子高，且分配的糖果数不超过下一个孩子的糖果数，则重新分配
                dp[i] = dp[i + 1] + 1

        # 返回所有孩子得到的糖果总数
        return sum(dp)

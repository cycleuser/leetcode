
class Solution:
    def tallestBillboard(self, rods):
        """
        :param rods: 列表，表示不同长度的钢筋（英文：List of integers representing the lengths of different rods）
        :return: 返回可以构建的最大高度差（英文：Return the maximum possible height difference that can be achieved by selecting a subset of rods）
        
        使用动态规划解决最大高度差问题。
        """
        dp = {0: 0}
        for x in rods:
            # 创建一个dp的临时副本，避免在迭代过程中修改原字典
            temp_dp = dp.copy()
            for d, h in temp_dp.items():
                # 更新以d+x为差异时的最大高度
                dp[d + x] = max(dp.get(d + x, 0), h)
                # 计算并更新以abs(d-x)为差异时的高度，取两者中的较大值
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), h + min(d, x))
        return dp[0]

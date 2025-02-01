
class Solution:
    # 定义解决方案类

    def flipLights(self, n: int, m: int) -> int:
        """
        :param n: 灯的数量 (最多考虑3个灯的情况)
        :param m: 操作次数
        :return: 不同的开关组合数量
        """

        # 只有当灯的数量不超过3时，才进行详细计算
        n = min(n, 3)

        # 计算不同的开关组合数：最多2^3种组合，加上多次操作后的额外组合数（这里假设为1+m*n）
        return min(1 << n, 1 + m * n)

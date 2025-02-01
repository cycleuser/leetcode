
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # 将输入的字符串n转换为整数
        n = int(n)

        # 计算log(n, 2)，作为循环上限，确保m范围合理
        for m in range(int(math.log(n, 2)), 1, -1):
            # 计算k的值，即等比序列的第一个项
            k = int(n ** (1/m))

            # 检查是否满足等比数列求和公式等于n，满足则返回k
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)

        # 如果没有找到满足条件的m，则返回n-1作为特殊情况处理
        return str(n-1)


from collections import Counter
import itertools

class Solution:
    def threeSumMulti(self, A, target):
        """
        :param A: List[int], 输入数组
        :param target: int, 目标和
        :return: int, 满足条件的三元组组合数
        
        使用计数器统计数组中每个元素的数量，通过组合计算满足目标和的三元组数量。
        """
        
        c = Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k:
                # 三个相同的数，组合公式：C(n, 3) = n * (n-1) * (n-2) / 6
                res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k:
                # 两个相同的数，一个不同的数，组合公式：C(n, 2) * n = n * (n-1) / 2
                res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j:
                # 三个不同且大于i和j的数，直接组合
                res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)

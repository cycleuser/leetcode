
class Solution:
    # 定义求子序列宽度和的解决方案类

    def sumSubseqWidths(self, A):
        """
        :type A: List[int]  # 输入列表A，包含整数元素
        :rtype: int         # 返回值为计算结果，取模10^9+7
        """
        A.sort()             # 对输入列表进行排序

        res = 0              # 初始化结果变量res为0
        
        for i in range(len(A)):
            # 每次循环将当前元素的贡献值加到结果中
            # 通过乘以2并减去和加上相应位置的元素实现子序列宽度累加
            res *= 2
            res -= A[i]
            res += A[~i]

        return res % (10**9+7)  # 返回结果对10^9+7取模后的值，确保结果在int范围内

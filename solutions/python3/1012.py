
class Solution(object):
    def numDupDigitsAtMostN(self, N: int) -> int:
        """
        :param N: 输入整数，范围在 [0, 2^31 - 1] 内
        :return: 不含重复数字的正整数个数，这些数小于或等于 N

        思路：
        1. 将输入转换为字符串形式以处理位数和重复字符。
        2. 计算小于给定数值的所有非重复数的数量。
        3. 通过逐位构建数来精确计算结果。
        """

        # 判断数字 n 是否包含重复的数字
        def has_repeated(n: int) -> bool:
            """
            :param n: 输入整数
            :return: 如果 n 包含重复数字，返回 True；否则返回 False
            """
            str_n = str(n)
            return len(set(str_n)) != len(str_n)

        # 计算 k 位非零起始的全排列数量
        def permutation(n: int, k: int) -> int:
            """
            :param n: 总数
            :param k: 需要选择的数量
            :return: k 位非重复数字组合的个数
            """
            prod = 1
            for i in range(k):
                prod *= (n - i)
            return prod

        # 计算 n 位非重复整数的数量（不以0开头）
        def n_digit_no_repeat(n: int) -> int:
            """
            :param n: 数字位数
            :return: n 位全排列非重复数字的个数，n >= 1
            """
            if n == 1:
                return 9  # 单一位数时从 1-9 中选
            else:
                return 9 * permutation(9, n - 1)

        N_str = str(N)
        n_digit = len(N_str)  # 计算位数
        digits = list(map(int, N_str))  # 将每一位转换为整数

        result = N - 1  # 初始结果：小于N的非重复数字个数

        prefix = 0
        for i in range(1, n_digit):  # 计算所有比给定数字少n位的非重复数字数量
            result -= n_digit_no_repeat(i)

        for i in range(n_digit):
            start = 1 if i == 0 and digits[i] > 0 else 0  # 处理最高有效位不能为零的情况

            for j in range(start, digits[i]):
                if has_repeated(prefix * 10 + j):  # 如果构建的前缀加上当前数字会导致重复，跳过
                    continue
                result -= permutation(9 - i, n_digit - 1 - i)  # 剩余位数的排列组合

            prefix = prefix * 10 + digits[i]  # 更新前缀

        return result + has_repeated(N)  # 返回最终结果，加上N本身是否含重复数字

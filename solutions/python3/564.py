
class Solution:
    def nearestPalindromic(self, S: str) -> str:
        """
        生成可能的回文数候选列表。
        
        :param S: 输入字符串，表示数字
        :return: 最接近输入数字且为回文数的字符串形式的数字
        """

        K = len(S)
        # 生成一些基本的候选值：比原数大/小1和比原数长度多一位或少一位的数字
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]

        prefix = S[:(K+1)//2]  # 获取前半部分作为回文数的前缀

        P = int(prefix)
        for start in map(str, (P-1, P, P+1)):
            candidates.append(start + (start[:-1] if K%2 else start)[::-1])  # 构造完整的回文数候选值

        def delta(x):
            """
            计算输入数字与目标数字之间的差值。

            :param x: 输入字符串形式的数字
            :return: 差值的绝对值
            """
            return abs(int(S) - int(x))

        ans = None  # 初始化最优解
        for cand in candidates:
            if cand != S and not cand.startswith('00'):  # 排除非法或相同情况
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand  # 更新最优解

        return ans


class Solution:
    def maxRepOpt1(self, S: str) -> int:
        """
        分析字符串S，找到最长的可以替换一个字符后的连续相同字符子串长度。
        
        中文注释：分析字符串S，找到最长的可以替换一个字符后的连续相同字符子串长度。
        """
        import itertools
        from collections import Counter

        # 使用groupby对字符串进行分组，并计算每个字母的连续出现次数
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        
        # 计算每个字母在S中出现的总次数
        count = Counter(S)
        
        # 初始化结果为第一个分组的最小替换长度
        res = max(min(k + 1, count[c]) for c, k in A)

        # 遍历A，检查是否可以通过替换一个字符来增加连续相同字符子串的长度
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # 如果当前分组中间仅有一个字符，并且前后两组字符相同，则考虑替换该单个字符
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))

        return res

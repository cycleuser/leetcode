
class Solution:
    # 定义一个类用于解决最小翻转单调递增字符串问题

    def minFlipsMonoIncr(self, s: str) -> int:
        # 初始化结果变量res和当前零的数量cur为s中"0"的个数
        res = cur = s.count("0")
        
        for c in s:  # 遍历字符串s中的每个字符c
            # 根据当前字符决定翻转后的最小值，更新res和cur
            res, cur = (res, cur + 1) if c == "1" else (min(res, cur - 1), cur - 1)
        
        return res  # 返回最小翻转次数

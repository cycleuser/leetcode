
class Solution:
    # 定义一个解决方案类

    def uniqueLetterString(self, S):
        # 初始化每个大写字母的索引数组为[-1, -1]
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        
        res = 0
        # 遍历字符串S中的每一个字符及其位置
        for i, c in enumerate(S):
            k, j = index[c]
            # 计算当前字符作为子串起始或结束的唯一字符串数量，并累加到结果中
            res += (i - j) * (j - k)
            # 更新该字符的最新位置
            index[c] = [j, i]

        # 遍历所有大写字母，计算剩余部分的贡献值
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        
        # 返回结果对10^9 + 7取模后的值
        return res % (10**9 + 7)


class Solution:
    # 定义一个解决方案类

    def minWindow(self, S: str, T: str) -> str:
        # 寻找字符串S中包含子串T的最小子串
        
        def dfs(i, j):
            """
            深度优先搜索，用于查找从索引i开始匹配T[j]及其之后的所有字符的最小起始位置
            :param i: 当前搜索起始索引
            :param j: 匹配模式字符串T中当前匹配到的位置
            :return: 从S中找到的第一个匹配子串起点索引
            """
            if j == len(T): 
                return i
            if (i, j) not in memo:
                ind = S.find(T[j], i + 1)
                # 如果找不到，设置一个非常大的值；否则递归调用dfs继续查找下一个匹配字符的位置
                memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]
        
        l, res, memo = float('inf'), '', {}
        # 初始化结果长度l为无穷大，结果res为空字符串，memo用于记忆化搜索
        for i, s in enumerate(S):
            if s == T[0]:
                # 如果当前字符与T的第一个字符匹配，则尝试从该位置开始查找最小子串
                j = dfs(i, 1)
                if j - i < l:
                    # 更新结果，如果找到更短的子串则替换
                    l, res = j - i, S[i:j + 1]
        return res  # 返回最小窗口子串

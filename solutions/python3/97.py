
class Solution:
    # 判断字符串s1和s2是否可以交错形成s3

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 使用记忆化搜索减少重复计算
        def dfs(i: int, j: int, k: int):
            if (i, j, k) not in memo:
                # 如果当前位置未被访问过，判断是否可以形成交错字符串
                memo[(i, j, k)] = (k >= l3 or  # s3的当前字符匹配结束情况
                                   (i < l1 and s3[k] == s1[i] and dfs(i + 1, j, k + 1)) or  # 尝试从s1中取字符
                                   (j < l2 and s3[k] == s2[j] and dfs(i, j + 1, k + 1)))  # 尝试从s2中取字符
            return memo[(i, j, k)]

        l1, l2, l3, memo = len(s1), len(s2), len(s3), {}  # 计算字符串长度并初始化记忆字典

        if l3 != l1 + l2:  # 初步验证s3的长度是否合理
            return False

        return dfs(0, 0, 0)  # 调用深度优先搜索从起点开始查找交错路径

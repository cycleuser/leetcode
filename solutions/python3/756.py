
class Solution:
    # Python 解决方案类

    def pyramidTransition(self, bottom, allowed):
        # 初始化字符集和允许的组合集合
        chars = 'ABCDEFG'
        allowed = set(allowed)

        def dfs(r, q, i):
            """
            :param r: 当前行字符串
            :param q: 下一行构建的字符串
            :param i: 当前行索引
            """
            # 如果当前行长度为1，表示已成功构建金字塔，返回True
            if len(r) == 1:
                return True

            for c in chars:
                # 检查当前字符组合是否在允许的集合中
                if r[i:i+2] + c in allowed and \
                        (i == len(r)-2 and dfs(q+c, "", 0) or dfs(r, q+c, i+1)):
                    return True
            return False

        # 开始深度优先搜索，返回是否可以成功构建金字塔
        return dfs(bottom, "", 0)

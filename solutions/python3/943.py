
class Solution:
    # 寻找最短超级字符串
    def shortestSuperstring(self, A):
        """
        :param A: 字符串列表
        :return: 最短的包含所有给定字符串的超级字符串
        """

        def merge(a, b):
            """
            将两个字符串合并，返回最大前缀重叠长度及剩余部分
            :param a: 首个字符串
            :param b: 后一个字符串
            :return: 最大前缀重叠长度和剩余部分组成的元组
            """
            for i in range(len(b), 0, -1):
                if a.endswith(b[:i]):
                    return i, b[i:]
            return 0, ''

        def dfs(sup, s, st):
            """
            深度优先搜索，用于寻找最短超级字符串
            :param sup: 当前构建的超级字符串部分
            :param s: 当前处理的字符串
            :param st: 剩余未使用字符串集合
            """
            if len(sup + "".join(st)) < len(res[0]):
                res[0] = sup + "".join(st)

            # 检查是否可以合并，继续搜索
            if st and any(new in st for new in merged[s][1:]):
                for new in merged[s][1:]:
                    if new in st:
                        dfs(sup + new[merged[s][0]:], new, st - {new})
            else:
                # 逐个尝试剩余字符串进行合并
                for nex in st:
                    for new in merged[nex][1:]:
                        if new in st:
                            dfs(sup + nex + new[merged[nex][0]:], new, st - {nex, new})

        # 计算两个字符串的最大重叠前缀长度和剩余部分
        merged = {}
        for a, b in itertools.combinations(A, 2):
            for a, b in ((a, b), (b, a)):
                s = merge(a, b)
                if a not in merged or s[0] > merged[a][0]:
                    merged[a] = [s[0], s[1]]
                elif s[0] == merged[a][0]:
                    merged[a].append(b)

        # 初始化结果集和剩余字符串集合
        res, st = ["".join(A)], set(A)
        for a in A:
            dfs(a, a, st - {a})

        return res[0]

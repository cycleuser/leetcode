
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        """
        计算给定数组A中可以构成平方和的排列数量
        
        参数:
        A (List[int]): 给定整数列表
        
        返回值:
        int: 可以构成平方和的排列数量
        """

        self.res = 0

        def dfs(cnt, num):
            """
            深度优先搜索，寻找合法路径
            
            参数:
            cnt (Counter): 当前元素使用情况计数器
            num (int): 当前节点值
            """
            if not cnt:
                # 所有元素都已使用完，找到一个有效排列
                self.res += 1
            for new in nex[num]:
                if cnt[new]:
                    # 使用当前新元素，并更新计数器
                    cnt[new] -= 1
                    if not cnt[new]:
                        cnt.pop(new)
                    dfs(cnt, new)
                    # 恢复状态
                    cnt[new] += 1

        from collections import Counter
        import itertools

        nex = collections.defaultdict(set)  # 邻接表，记录可以构成平方和的相邻关系
        cnt = Counter(A)  # 记录当前元素使用情况计数器

        # 构建邻接表nex
        for a, b in itertools.permutations(A, 2):
            if not (a + b) ** 0.5 % 1:  # 判断是否能构成平方和
                nex[a].add(b)
                nex[b].add(a)

        # 开始深度优先搜索，遍历所有起始点
        for a in set(A):
            cnt[a] -= 1
            if not cnt[a]:
                cnt.pop(a)
            dfs(cnt, a)
            cnt[a] += 1

        return self.res

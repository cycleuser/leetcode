
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        
        # 如果只有一个学期，直接返回1
        if N == 1:
            return 1
        
        from collections import defaultdict

        # 构建有向图表示先修课程关系
        graph = defaultdict(list)
        for p, q in relations:
            graph[q-1].append(p-1)

        def need_semesters(n: int) -> int:
            """
            :param n: node index
            :return: minimum semesters needed to complete all courses starting from node n
            """
            if dp[n] > 0:   # 节点已被访问过
                return dp[n]
            if dp[n] == -1: # 正在访问该节点，存在环!
                return -1

            # 标记当前节点为正在访问状态
            dp[n] = -1 
            res = 0
            for p in graph[n]:
                a = need_semesters(p)
                if a == -1:
                    return -1
                res = max(res, a)

            # 计算完成所有课程需要的最短学期数，并保存到dp数组中
            dp[n] = res + 1
            return dp[n]

        # 初始化dp数组，用于记录节点状态和所需学期数
        dp = [0]*N

        for n in range(N):
            if need_semesters(n) == -1:
                return -1
        
        return max(dp)

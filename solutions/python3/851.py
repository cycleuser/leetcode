
class Solution:
    # 定义Solution类，用于解决富人和安静程度的问题

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # 初始化邻接表、记忆化字典和结果列表
        edges, memo, res = collections.defaultdict(list), {}, [i for i in range(len(quiet))]

        # 构建有向图，将富人关系存储在edges中
        for r, p in richer: 
            edges[p].append(r)

        # 定义深度优先搜索函数explore
        def explore(i):
            if i in memo:
                return memo[i]
            
            cur_min = i  # 当前节点最小安静值索引，初始化为自身

            # 遍历当前节点的所有邻居节点
            for v in edges[i]:
                # 递归探索邻居节点
                cur = explore(v)
                if quiet[cur] < quiet[cur_min]: 
                    cur_min = cur
            
            # 将结果存储在memo和res中
            res[i] = memo[i] = cur_min

            return cur_min
        
        # 对每个节点执行深度优先搜索
        for i in range(len(quiet)): explore(i)
        
        # 返回最终的结果列表
        return res

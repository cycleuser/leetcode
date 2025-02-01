
class Solution:
    def shortestPathLength(self, graph):
        """
        初始化记忆集合、最终状态和队列。
        
        :param graph: List[List[int]] - 图的邻接表表示
        """
        memo, final_state, q = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        
        while q:
            node, steps, state = q.popleft()
            
            # 如果当前状态等于最终状态，返回步数
            if state == final_state: 
                return steps
            
            # 遍历当前节点的邻接节点
            for v in graph[node]:
                # 构建新的状态并检查是否已经访问过
                new_state = state | 1 << v
                if (new_state, v) not in memo:
                    q.append((v, steps + 1, new_state))
                    memo.add((new_state, v))

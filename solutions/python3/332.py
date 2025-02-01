
class Solution:
    def findItinerary(self, tickets):
        # 初始化图、栈和已到达路径
        graph, stack, reached = collections.defaultdict(list), ["JFK"], []
        
        # 将航班信息按起点排序并加入图中
        for a, b in tickets: 
            heapq.heappush(graph[a], b)
        
        # 使用深度优先搜索遍历路径
        while stack:
            if graph[stack[-1]]:  # 如果当前节点还有未访问的邻接点
                stack.append(heapq.heappop(graph[stack[-1]]))  # 推入下一个目的地
            else:  # 当前节点所有邻接点都已访问完，加入已到达路径
                reached.append(stack.pop())
        
        return reached[::-1]  # 反转路径以获得正确的飞行顺序

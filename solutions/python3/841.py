
class Solution:
    # 判断是否可以访问所有房间

    def canVisitAllRooms(self, rooms):
        # 初始化可访问集合和栈，起点为0
        pool, stack = set(range(len(rooms))), [0]
        
        while stack: 
            # 从当前栈顶元素移除，并检查其相邻节点
            pool.discard(stack[-1])
            for nex in rooms[stack.pop()]:
                if nex in pool: 
                    stack.append(nex)
                    
        # 如果所有房间都被访问过，则返回True
        return not pool

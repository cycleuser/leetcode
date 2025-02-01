
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        判断是否可以从source节点逃到target节点，给定被阻塞的区域blocked。
        
        参数：
            blocked: 被阻塞的格子列表
            source: 源点坐标 [x, y]
            target: 目标点坐标 [x, y]
            
        返回值：
            如果可以从source逃到target，返回True；否则返回False。
        """
        
        if not blocked:
            return True  # 若没有被阻塞的区域，则可以直接到达目标
        blocked = set(map(tuple, blocked))
        
        def check(blocked, start: List[int], end: List[int]) -> bool:
            """
            检查从start是否能到达end
            
            参数：
                blocked: 被阻塞的格子列表
                start: 当前节点坐标 [x, y]
                end: 目标点坐标 [x, y]
                
            返回值：
                如果可以从start逃到end，返回True；否则返回False。
            """
            
            si, sj = start  # 起始位置
            ti, tj = end    # 结束位置
            
            level = 0
            q = collections.deque([(si,sj)])  # 队列用于BFS
            vis = set()                       # 记录已访问的格子
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if i == ti and j == tj: return True   # 到达目标点，返回True
                    
                    for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):  # 遍历四个方向
                        if (0<=x<10**6) and (0<=y<10**6) and \
                           (x,y) not in vis and (x,y) not in blocked:
                            vis.add((x,y))       # 标记已访问
                            q.append((x,y))      # 入队
                
                level += 1
                if level == len(blocked): break   # 若访问的步数达到被阻塞格子的数量，提前终止
            
            else:                               # 当while循环正常结束（非break）
                return False                    # 没有到达目标点
        
        return check(blocked, source, target) and check(blocked, target, source)

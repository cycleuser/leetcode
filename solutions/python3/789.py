
class Solution:
    # 定义一个Solution类，包含escapeGhosts方法用于判断是否能成功逃脱幽灵

    def escapeGhosts(self, ghosts, target):
        # 计算目标位置到原点的距离
        d = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            # 检查每个幽灵的位置，判断是否存在一条路径可以比幽灵更快到达目标
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= d: 
                return False
        
        # 如果所有幽灵都无法在更短时间内达到目标，则返回True
        return True

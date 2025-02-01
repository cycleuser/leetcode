
class Solution:
    def openLock(self, deadends, target):
        """
        中文注释：定义一个解决方案类，包含openLock方法。
        
        英文注释: Define a solution class with an openLock method.
        """

        # 初始化移动集合、队列、计数器和转盘状态映射
        moved, q, cnt, move = set(deadends), ["0000"], 0, {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        
        # 检查起始状态是否在禁用列表中
        if "0000" in moved:
            return -1
        
        # 广度优先搜索遍历所有可能的转盘状态
        while q:
            new = []
            
            # 增加当前步数计数器
            cnt += 1
            
            # 遍历队列中的每个字符串（当前状态）
            for s in q:
                # 遍历字符串的每一位字符
                for i, c in enumerate(s):
                    # 尝试向上和向下翻转转盘
                    for cur in (s[:i] + move[c][0] + s[i + 1:], s[:i] + move[c][1] + s[i + 1:]):
                        # 如果当前状态不在禁用列表中
                        if cur not in moved:
                            # 判断是否为目标状态，如果是则返回步数计数器值
                            if cur == target:
                                return cnt
                            # 否则将新状态加入队列并标记为已访问
                            new.append(cur)
                            moved.add(cur)
            
            # 更新队列为当前的新的转盘状态列表
            q = new
        
        # 如果无法到达目标状态，返回-1
        return -1

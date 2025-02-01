
class Solution:
    # 定义一个类来解决最少打破的砖墙问题

    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict  # 导入defaultdict用于统计边界点出现次数
        
        m = len(wall)  # 墙的高度
        sm = sum(wall[0])  # 第一行砖块的总长度，用于判断是否到达墙的尽头
        cnt = defaultdict(int)  # 使用defaultdict来记录每个边界点出现的次数

        for i in range(m):
            x = 0
            for num in wall[i]:
                x += num  # 累加当前砖块长度
                if x != sm:  # 如果还没有到达墙的尽头
                    cnt[x] += 1  # 记录边界点出现次数

        mx = 0  # 初始化最大边界点数为0
        
        for i in range(m):
            x = 0
            for num in wall[i]:
                x += num  # 累加当前砖块长度
                mx = max(mx, cnt[x])  # 更新最大边界点数

        return m - mx  # 返回最小打破的砖墙次数，即总高度减去最大边界点数

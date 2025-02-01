
class Solution:
    # 定义一个解决方案类，用于解决求座位最大最远距离的问题

    def maxDistToClosest(self, seats):
        d = {}  # 用于存储每个空位到最近人的最大距离
        res = l = left = r = right = 0
        
        # 正向遍历座位列表，更新左侧连续空位数并记录最左端的位置
        for i, s in enumerate(seats):
            if not s and left: 
                d[i] = l = l + 1
            elif s: 
                l, left = 0, 1
        
        # 反向遍历座位列表，更新右侧连续空位数并记录最右端的位置
        for i in range(len(seats) - 1, -1, -1):
            if not seats[i] and right and (i not in d or d[i] > r): 
                d[i] = r = r + 1  
            elif seats[i]: 
                r, right = 0, 1
        
        # 返回所有记录的最大值，即为最远距离
        return max(d.values())

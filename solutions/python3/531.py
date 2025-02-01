
class Solution:
    # 寻找孤独像素 - 找到满足条件的黑色像素数量
    
    def findLonelyPixel(self, grid: List[List[str]]) -> int:
        # 使用defaultdict存储每行和每列中'B'的位置
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        
        m, n = len(grid), len(grid[0])  # 获取矩阵的行数m和列数n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    rows[i].append(j)  # 将该位置的列索引加入对应行的列表
                    cols[j].append(i)  # 将该位置的行索引加入对应列的列表
        
        res = 0  # 初始化结果计数器
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B' and len(rows[i]) == 1 and rows[i][0] == j and \
                   len(cols[j]) == 1 and cols[j][0] == i:
                    # 检查当前'B'是否为孤独像素
                    res += 1
        
        return res  # 返回满足条件的黑色像素数量

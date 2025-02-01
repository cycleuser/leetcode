
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        给定一个整数矩阵，按螺旋顺序返回其元素。
        
        中文注释：给定一个整数矩阵，按螺旋顺序返回其元素。
        """
        res = []
        seen = set()
        
        """
        定义递归深度优先搜索函数，用于模拟螺旋遍历过程。
        
        中文注释：定义递归深度优先搜索函数，用于模拟螺旋遍历过程。
        """
        def dfs(i, j, d):
            seen.add((i, j))
            res.append(matrix[i][j])
            
            if d == 'r':  # 右
                next_dir = 'd'
                if j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, d)
                elif i + 1 < m and (i + 1, j) not in seen:  # 下
                    next_dir = 'd'
                    dfs(i + 1, j, next_dir)
            elif d == 'd':  # 下
                next_dir = 'l'
                if i + 1 < m and (i + 1, j) not in seen:
                    dfs(i + 1, j, d)
                elif j - 1 >= 0 and (i, j - 1) not in seen:  # 左
                    next_dir = 'l'
                    dfs(i, j - 1, next_dir)
            elif d == 'l':  # 左
                next_dir = 'u'
                if j - 1 >= 0 and (i, j - 1) not in seen:
                    dfs(i, j - 1, d)
                elif i - 1 >= 0 and (i - 1, j) not in seen:  # 上
                    next_dir = 'u'
                    dfs(i - 1, j, next_dir)
            else:  # u（上）
                if i - 1 >= 0 and (i - 1, j) not in seen:
                    dfs(i - 1, j, d)
                elif j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, 'r')
        
        """
        如果输入矩阵为空，直接返回空列表。
        
        中文注释：如果输入矩阵为空，直接返回空列表。
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        
        """
        从 (0, 0) 点开始，初始方向为 'r'（右）进行遍历
        
        中文注释：从 (0, 0) 点开始，初始方向为 'r'（右）进行遍历
        """
        dfs(0, 0, 'r')
        
        return res


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        计算在n×n棋盘上放置不冲突的皇后的方法总数。
        
        Parameters:
            n (int): 棋盘大小，也是皇后的数量
        
        Returns:
            int: 放置方法的数量
        """
        res = [0]  # 用于存储结果

        def dfs(i, l, r, m):
            """
            深度优先搜索函数。
            
            Parameters:
                i (int): 当前行索引，表示当前处理的是第i+1行
                l, r (list of int): 分别代表左斜线和右斜线的掩码状态
                m (list of int): 用于存储每一列的状态（1为放置了皇后，0为空）
            """
            if i == n:  # 当处理完最后一行时
                res[0] += 1  # 结果计数加一
            else:
                l = l[1:] + [0]  # 更新左斜线掩码状态
                r = [0] + r[:-1]  # 更新右斜线掩码状态

                for j in range(n):  # 遍历当前行的每个列位置
                    if m[j] == l[j] == r[j] == 0:  # 当前位置可以放置皇后
                        m[j] = l[j] = r[j] = 1  # 放置皇后，并更新掩码状态
                        dfs(i + 1, l, r, m)  # 处理下一行
                        m[j] = l[j] = r[j] = 0  # 恢复状态，回溯

        dfs(0, [0]*n, [0]*n, [0]*n)
        return res[0]

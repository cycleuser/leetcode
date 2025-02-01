
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        定义一个深度优先搜索函数，用于检查每种方向上是否存在皇后。
        
        :param dr: 方向增量的行变化值
        :param dc: 方向增量的列变化值
        :param r: 当前行索引
        :param c: 当前列索引
        """
        def dfs(dr, dc, r, c):
            # 确保在棋盘范围内
            while 0 <= r <= 7 and 0 <= c <= 7:
                if (r, c) in q:  # 检查当前位置是否是皇后的位置
                    res.append([r, c])  # 如果是，添加结果并结束搜索
                    break
                r += dr  # 向指定方向移动一行
                c += dc  # 向指定方向移动一列
        
        # 将所有皇后的坐标加入集合q以O(1)时间复杂度查找
        q = set((r, c) for r, c in queens)
        
        res = []  # 存储结果
        
        # 遍历8个可能的方向
        for dr, dc in (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1):
            # 对每个方向进行深度优先搜索，从king的位置开始
            dfs(dr, dc, *king)
        
        return res  # 返回结果列表

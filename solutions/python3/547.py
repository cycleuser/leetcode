
class Solution:
    def findCircleNum(self, m):  # 寻找朋友圈数量

        """
        :param m: 友情关系矩阵，m[i][j] = 1 表示 i 和 j 是朋友，0 则不是
        :return: 返回朋友圈的数量
        """

        res, n = 0, len(m)  # 初始化结果和矩阵大小
        
        def explore(i):  # 深度优先搜索函数
            """
            :param i: 当前要探索的朋友编号
            :return: 无返回值，用于标记已访问过的节点
            """
            m[i][i] = 0  # 标记当前节点为已访问
            for j in range(n):  # 遍历所有节点
                if i != j and m[i][j] == m[j][j] == 1:  # 如果是朋友且未访问过
                    explore(j)  # 递归探索

        for i in range(n):  # 遍历每个可能的起始点
            if m[i][i] == 1:  # 初始节点为1，表示是一个新的朋友圈起点
                explore(i)
                res += 1  # 新发现一个朋友圈
        
        return res  # 返回朋友圈的数量

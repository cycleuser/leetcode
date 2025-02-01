
class Solution:
    # 定义一个解决方案类
    
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        """
        :param N: 花园的数量
        :param paths: 两个花园之间路径的列表，每个元素是一个包含两个整数的列表[x, y]表示x和y直接有一条路径相连
        :return: 返回一个长度为N的列表，表示每个花园种植的不同花的颜色编号（1-4）
        """
        
        res = [0] * N  # 初始化结果列表，初始值为0
        G = [[] for i in range(N)]  # 构建邻接表，用于存储每朵花相邻的其他花朵
        
        # 遍历路径列表，构建邻接表
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        
        # 对每个花园，选择未使用的颜色填充到结果中
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        
        return res  # 返回结果列表

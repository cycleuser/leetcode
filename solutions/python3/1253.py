
class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        """
        构造一个2行colsum长度的矩阵，使得每列的和符合给定的upper和lower限制

        :param upper: 上半部分的目标和
        :param lower: 下半部分的目标和
        :param colsum: 每列目标和组成的列表
        :return: 符合条件的2行矩阵，否则返回空列表
        """
        res = [[0] * len(colsum) for _ in range(2)]  # 初始化结果矩阵
        
        for j, sm in enumerate(colsum):
            if sm == 2:
                # 当列和为2时，同时填充上半部分和下半部分
                if upper == 0 or lower == 0:
                    return []  # 如果某一部分已经无法满足要求，则直接返回空列表
                upper -= 1
                lower -= 1
                res[0][j] = res[1][j] = 1
        
            elif sm:  # 当列和大于0时，根据上下部分剩余容量选择填充位置
                if upper == lower == 0:
                    return []  # 如果剩余容量都为0，则直接返回空列表
                
                if upper >= lower:
                    # 尽可能多地填满上半部分
                    upper -= 1
                    res[0][j] = 1
                else:
                    # 剩余填充下半部分
                    lower -= 1
                    res[1][j] = 1
        
        return res if upper == lower == 0 else []  # 检查是否所有容量都已满足，否则返回空列表

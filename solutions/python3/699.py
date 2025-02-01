
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        解决问题：给定一系列方块的起始位置和大小，计算每个时刻的最大高度。
        
        :param positions: 一个二维列表，表示每个方块的左边界和宽度
        :return: 返回一个一维列表，表示每个时间点的最大高度
        
        思路分析：
            - 使用线段树来维护每个区间的最大高度
            - 对于每一个新出现的方块，找到它覆盖的所有区间，并更新这些区间的最大高度
            - 通过二分查找快速定位要处理的区间
        """
        height = [0]  # 初始化高度列表
        pos = [0]     # 初始化位置列表
        res = []      # 存储结果的最大高度
        max_h = 0     # 当前最大高度

        for left, side in positions:  # 遍历每个方块
            i = bisect.bisect_right(pos, left)  # 找到大于等于left的第一个位置的索引
            j = bisect.bisect_left(pos, left + side)  # 找到最后一个小于等于left+side-1的位置的索引

            high = max(height[i - 1:j] or [0]) + side  # 计算当前方块的最大高度
            
            pos[i:j] = [left, left + side]  # 更新位置列表
            height[i:j] = [high, height[j - 1]]  # 更新高度列表

            max_h = max(max_h, high)  # 更新最大高度
            res.append(max_h)         # 添加到结果中
        
        return res  # 返回结果

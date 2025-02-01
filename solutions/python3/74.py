
class Solution:
    """定义一个Solution类，包含searchMatrix方法用于在矩阵中查找目标值"""

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 将二维列表展平为一维列表，并使用二分法查找目标值
        flat_list = list(itertools.chain(*matrix))
        
        # 使用bisect模块的bisect函数进行二分查找，返回插入点索引减1的位置
        index = bisect.bisect(flat_list, target) - 1
        
        # 判断找到的目标值是否等于目标值，并返回结果
        return flat_list[index] == target if index < len(flat_list) else False

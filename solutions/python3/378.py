
class Solution:
    # 定义一个类用于解决查找矩阵中第K小元素的问题

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 使用itertools.chain将二维列表展平为一维，然后进行排序
        # 通过sorted函数对所有元素进行升序排列
        return sorted(itertools.chain(*matrix))[k - 1]  # 返回第K小的元素（注意索引从0开始）

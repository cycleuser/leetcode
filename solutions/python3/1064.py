
class Solution:
    # 定义一个查找固定点的方法，输入是一个整数列表A，输出是第一个固定点的索引或-1
    def fixedPoint(self, A: List[int]) -> int:
        # 使用列表生成式找到所有满足条件的固定点索引，如果找不到则返回-1
        return ([i for i in range(len(A)) if A[i] == i] + [-1])[0]

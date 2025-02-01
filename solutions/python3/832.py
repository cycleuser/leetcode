
class Solution(object):
    # 定义一个类来解决问题

    def flipAndInvertImage(self, A):
        # 对每个二维数组A中的每一行进行翻转并逐位取反
        
        return [[1 - x for x in A[i][::-1]] for i in range(len(A))]
        # 通过列表推导式实现：先对每行进行反转[::-1]，然后逐元素取反1-x

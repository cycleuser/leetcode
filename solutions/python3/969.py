
class Solution:
    # Python 解决翻转数组使有序的问题

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []  # 用于存储每次需要执行的操作的反转次数
        
        for x in range(len(A), 1, -1):  # 从数组长度递减到2
            i = A.index(x)  # 找到当前最大值x的位置
            
            # 将最大值翻转至开头，再整体翻转至指定位置
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        
        return res  # 返回所需的操作序列

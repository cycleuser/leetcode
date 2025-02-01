
class Solution:
    def longestMountain(self, A: List[int], res: int = 0) -> int:
        """
        计算数组A中最长的山脉长度。
        山脉定义为元素严格递增后严格递减的一段。

        :param A: 输入整数列表
        :param res: 结果变量，初始值为0
        :return: 最长山脉的长度

        1. 遍历数组A，从第二个元素开始到倒数第二个结束。
        2. 如果当前元素是递增起点（比前一个大且比后一个小）：
           - 找到递增起点左侧边界l
           - 找到递减终点右侧边界r
           - 更新结果res为最大值
        """
        for i in range(1, len(A) - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                l = r = i
                # 向左找到递增起点
                while l and A[l] > A[l - 1]: 
                    l -= 1
                # 向右找到递减终点
                while r + 1 < len(A) and A[r] > A[r + 1]: 
                    r += 1
                if r - l + 1 > res: 
                    res = r - l + 1
        return res

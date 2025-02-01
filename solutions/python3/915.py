
class Solution:
    def partitionDisjoint(self, A: list[int]) -> int:
        """
        分区最小值问题：找到一个分区点，使得左边的最大值小于等于右边的最小值。
        
        参数：
            A (list[int]): 输入整数列表
        
        返回：
            int: 能满足条件的分区点索引（从1开始）
        """

        rMin, lMax = [0] * len(A), [0] * len(A)  # 初始化左右最小和最大值数组
        mx, mn = -float("inf"), float("inf")   # 初始化全局最大值和最小值

        # 前向遍历，填充lMax数组，表示从左到i的最大值
        for i, num in enumerate(A):
            mx = max(mx, num)
            lMax[i] = mx 

        # 后向遍历，填充rMin数组，表示从i到右的最大值
        for i in range(len(A) - 1, -1, -1):
            mn = min(mn, A[i])
            rMin[i] = mn 
        
        # 查找满足条件的分区点
        for i in range(len(A) - 1):
            if lMax[i] <= rMin[i + 1]:
                return i + 1

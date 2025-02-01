
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        英文注释：定义一个方法largestPerimeter，输入一个整数列表A，返回由这三个元素组成的三角形的周长最大值。
        
        中文注释：定义一个方法largestPerimeter，输入一个整数列表A，返回由这三个元素组成的三角形的周长最大值。
        """
        A.sort()  # 对数组进行排序
        return ([0] + [a + b + c for a, b, c in zip(A, A[1:], A[2:]) if c < a + b])[-1]  # 遍历所有可能的三角形组合，返回最大周长


class Solution:
    # 定义一个类来解决最接近点对的问题

    def kClosest(self, points, K):
        # 返回points中与原点最接近的K个点
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:K]
        # 使用sorted函数，通过计算每个点到原点的距离平方来排序，并返回前K个点

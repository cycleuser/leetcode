
class Solution(object):

    def outerTrees(self, points):
        """
        计算二维点集的凸包。
        
        输入：一个表示点对的可迭代序列，形式为 (x, y)。
        输出：按照逆时针顺序列出凸包的顶点，从最左边（或y坐标最小）的顶点开始。
        实现 Andrew 的单调链算法。复杂度为 O(n log n)。
        """

        # 按字典序排序点对，并去除重复项以处理仅有一个独特点的情况。
        points = sorted(points, key=lambda p: (p.x, p.y))

        # 边缘情况：无点或单个点（可能多次出现）。
        if len(points) <= 1:
            return points

        # 计算 OA 和 OB 向量的叉积，即 OAB 在三维空间中的向量积的 z 分量。
        # 返回正值表示逆时针转向，负值表示顺时针转向，零表示共线。
        def cross(o, a, b):
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

        # 构建下凸包
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # 构建上凸包
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # 下凸包和上凸包的组合构成完整的凸包。
        # 每个列表的最后一项重复，因此需要去除。
        return list(set(lower[:-1] + upper[:-1]))

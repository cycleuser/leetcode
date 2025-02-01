
class Solution:
    # 定义查找根节点的函数，返回给定字符对应的最小等价类代表字母
    def root(self, c: str) -> str:
        return c if parent[c] == c else self.root(parent[c])

    # 初始化每个小写字母为其自身父节点
    parent = {s: s for s in string.ascii_lowercase}

    # 遍历字符串A和B，合并它们对应的等价类
    for a, b in zip(A, B):
        p1, p2 = self.root(a), self.root(b)
        if p1 <= p2:
            parent[p2] = p1  # 将较大的等价类的父节点设为较小的等价类的根节点
        else:
            parent[p1] = p2

    # 遍历字符串S，返回每个字符对应的最小等价类代表字母构成的新字符串
    return ''.join(self.root(s) for s in S)

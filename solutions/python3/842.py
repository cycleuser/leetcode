
class Solution:
    # 初始化方法，用于生成可能的起始数字对
    def getStarter(self):
        arr = []
        for i in range(1, len(self.S) - 1):
            for j in range(i + 1, len(self.S)):
                s1, s2 = self.S[:i], self.S[i:j]
                if (s1[0] == "0" and len(s1) > 1) or (s2[0] == "0" and len(s2) > 1):
                    continue
                arr.append((int(s1), int(s2), j))
        return arr

    # 深度优先搜索方法，用于寻找满足Fibonacci序列条件的数字序列
    def dfs(self, arr, i):
        if i == len(self.S):
            return arr
        sm = arr[-2] + arr[-1]
        l = len(str(sm))
        new = int(self.S[i:i + l])
        # 检查新加入的数是否符合Fibonacci序列条件，并递归调用dfs
        return (new == sm and 0 <= sm < self.mx) and dfs(arr + [new], i + l)

    # 主方法，用于拆分字符串为满足Fibonacci序列的数字列表
    def splitIntoFibonacci(self, S):
        q, self.mx = self.getStarter(), 2 ** 31 - 1
        for p1, p2, i in q:
            seq = self.dfs([p1, p2], i)
            if seq:
                return seq
        return []

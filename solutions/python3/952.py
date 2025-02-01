
class Solution:
    def largestComponentSize(self, A):
        """
        初始化并查集和质因数映射字典。
        :param A: 非空整数数组，表示集合中的元素。
        """

        def find(i):
            """
            查找元素i的根节点，并进行路径压缩。
            :param i: 从0开始的索引
            """
            return i if i == parent[i] else find(parent[i])

        def prime_factors(n):  
            """
            获取n的所有质因数（重复的不重复添加）。
            :param n: 需要分解质因数的整数
            """
            res = set()
            while n % 2 == 0: 
                res.add(2)
                n //= 2
            for i in range(3, int(n**0.5) + 1, 2): 
                while n % i== 0: 
                    res.add(i) 
                    n //= i 
            if n > 2: 
                res.add(n)
            return res

        parent, dic = list(range(len(A))), {} 
        # 将每个元素与其质因数进行关联，并通过并查集将具有相同质因数的元素连通
        for i, n in enumerate(A):
            for p in prime_factors(n):
                if p in dic:
                    parent[find(i)] = find(dic[p])
                dic[p] = i

        # 最终计算每个联通分量的大小，并返回最大的连通分量的大小。
        for i, x in enumerate(parent):
            parent[i] = find(x)
        
        return max(collections.Counter(parent).values())

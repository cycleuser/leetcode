
class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 对输入数组A进行排序，便于后续处理
        A.sort()
        
        # 初始化集合、结果计数器和字典结构
        nums, res, trees, factors = set(A), 0, {}, collections.defaultdict(set)
        
        # 遍历每个元素作为根节点
        for i, num in enumerate(A):
            # 对于当前根节点num，寻找可以作为其因子的其他数n
            for n in A[:i]:
                if num % n == 0 and num // n in nums:
                    factors[num].add(n)
        
        # 遍历每个根节点并计算可能的树的数量
        for root in A:
            trees[root] = 1  # 基础情况：单个节点
            for fac in factors[root]:
                # 累加因子及其对应子树数量的乘积作为当前节点的子树数量
                trees[root] += trees[fac] * trees[root // fac]
        
        # 返回结果，注意取模以符合问题要求
        return sum(trees.values()) % ((10 ** 9) + 7)

    
class Solution:
    def numTrees(self, n: int) -> int:
        """
        计算n个节点的二叉搜索树的数量。
        
        参数:
            n (int): 节点数量
        
        返回:
            int: 二叉搜索树的数量
        """
        if n <= 1:
            return 1
        
        catalan = [0] * (n + 1)
        # 初始化卡特兰数的前两个值
        catalan[0], catalan[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(i):
                # 计算第i个节点时的卡特兰数值
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        return catalan[n]
    

class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        使用贪心算法计算最多可以放置多少层

        Greedy algorithm to calculate the maximum number of layers that can be placed.
        """
        sm = 0  # 当前累加和
        res = 0  # 结果，表示最多的层数
        
        for i in range(1, n + 1):
            sm += i  # 累加当前层的硬币数
            if sm > n:  # 如果当前累加和超过n，则跳出循环
                break
            res += 1  # 层数加一
            
        return res  # 返回结果

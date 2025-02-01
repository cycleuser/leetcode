
class Solution:
    # 定义一个类来解决数的平方表示问题

    def numSquares(self, n):
        # 初始化候选集合q为所有小于等于n的平方数，并初始化步数move为1
        q, move = {i ** 2 for i in range(1, int(n ** 0.5) + 1)}, 1
        
        # 定义硬币集coins，即候选集合q的副本
        coins = set(q)
        
        # 当候选集合q非空时循环
        while q:
            # 如果目标值n在候选集合q中，则返回当前步数move
            if n in q: 
                return move
            
            # 更新候选集合q为新的候选集，并增加一步
            q = {sm + c for sm in q for c in coins} - q
            move += 1

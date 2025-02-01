
class Solution:
    # 判断是否可以跳跃到所有石头上

    def canCross(self, stones):
        # 使用字典进行记忆化搜索，存储已经计算过的结果以提高效率
        memo, stones, target = {}, set(stones), stones[-1]
        
        def dfs(unit, last):
            """
            unit: 当前所在位置
            last: 上一次跳跃的步数
            """
            # 如果当前位置等于目标位置，则成功返回 True
            if unit == target:
                return True
            
            # 如果该状态未被计算过，进行深度优先搜索
            if (unit, last) not in memo:
                # 尝试不同的跳跃步数
                memo[(unit, last)] = any(dfs(unit + move, move) for move in (last - 1, last, last + 1) 
                                        if move and unit + move in stones)
            
            return memo[(unit, last)]
        
        # 如果起始位置不是 1，则无法开始跳跃
        return dfs(1, 1) if 1 in stones else False

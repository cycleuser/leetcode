    
class Solution:
    def bagOfTokensScore(self, tokens: list[int], P: int) -> int:
        """
        :type tokens: List[int] # 令牌列表
        :type P: int           # 玩家当前得分
        :rtype: int            # 最大分数
        
        思路：对令牌进行排序，优先使用较小的令牌来增加分数，遇到无法使用的较大令牌时，
              尽量通过之前获得的分数减去一个较大的令牌来继续游戏。
        """
        tokens.sort()  # 对令牌列表进行升序排序
        l, r, score = 0, len(tokens) - 1, 0  # 初始化双指针和得分
        
        while l <= r:
            if P >= tokens[l]:  # 当前得分足够使用最小的令牌时
                P -= tokens[l]  # 使用该令牌，减少当前得分
                score += 1      # 增加分数
                l += 1          # 移动左指针
            elif score and l != r:  # 分数充足且左右指针未相遇
                P += tokens[r]     # 使用最大的令牌增加当前得分
                score -= 1         # 减少分数
                r -= 1             # 移动右指针
            else:
                break               # 无法继续游戏，退出循环
        
        return score              # 返回最大分数
    
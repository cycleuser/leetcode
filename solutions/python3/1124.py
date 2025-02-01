
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
        初始化结果和当前得分，以及一个字典用于记录分数出现的最早索引。
        
        :param hours: 工作小时数列表
        :return: 最长有效工作时间间隔
        """
        res = score = 0
        seen = {}
        
        # 遍历每个工作小时数
        for i, h in enumerate(hours):
            # 更新当前得分：加班加1，减班减1
            score += 1 if h > 8 else -1
            
            # 如果当前得分为正，则更新最长有效间隔
            if score > 0:
                res = i + 1
            
            # 记录当前分数首次出现的索引
            seen.setdefault(score, i)
            
            # 更新最长有效间隔：若当前得分-1在字典中存在，说明有一段得分为正
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        
        return res


class Solution(object):
    """
    解决方案类，用于求解最大重复次数问题。
    """

    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 记录s2_idx在s1_round中出现的位置及对应的s2_round
        start = {}
        s1_round, s2_round, s2_idx = 0, 0, 0
        
        while s1_round < n1:
            s1_round += 1
            for ch in s1:
                # 如果当前字符匹配，则移动s2_idx
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    # 检查是否已完整匹配一个s2字符串
                    if s2_idx == len(s2):
                        s2_round += 1
                        s2_idx = 0
            
            # 如果之前已经遇到过相同s2_idx，则找到了循环节
            if s2_idx in start:
                prev_s1_round, prev_s2_round = start[s2_idx]
                circle_s1_round, circle_s2_round = s1_round - prev_s1_round, s2_round - prev_s2_round
                
                # 计算完整周期数量并加上剩余部分
                res = (n1 - prev_s1_round) // circle_s1_round * circle_s2_round
                left_s1_round = (n1 - prev_s1_round) % circle_s1_round + prev_s1_round
                for key, val in start.items():
                    if val[0] == left_s1_round:
                        res += val[1]
                        break
                
                return res // n2
            
            # 记录当前状态，供后续循环检查使用
            else:
                start[s2_idx] = (s1_round, s2_round)
        
        # 如果没有找到完整周期，则直接计算结果
        return s2_round // n2

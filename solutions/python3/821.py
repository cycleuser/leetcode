    
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        """
        :type S: str         # 输入字符串S
        :type C: str         # 目标字符C
        :rtype: List[int]    # 返回列表，表示每个位置到最近的字符C的距离
        """
        char1, char2, diff1, diff2, res = False, False, 0, 0, [None] * len(S)
        
        for i in range(len(S)):
            if char1: 
                res[i], diff1 = min(res[i], diff1 + 1) if res[i] else diff1 + 1, diff1 + 1
            if S[i] == C: 
                diff1, res[i], char1 = 0, 0, True  
            
            if char2: 
                res[len(S) - 1 - i], diff2 = min(res[len(S) - 1 - i], diff2 + 1) if res[len(S) - 1 - i] else diff2 + 1, diff2 + 1
            if S[len(S) - 1 - i] == C: 
                diff2, res[len(S) - 1 - i], char2 = 0, 0, True
        
        return res
    
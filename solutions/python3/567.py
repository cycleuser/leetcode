
class Solution:
    # 检查s1是否为s2的排列组合
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False  # 如果s1长度大于s2，直接返回False
        
        from collections import defaultdict
        dic = defaultdict(int)
        
        # 预处理窗口内字符频率
        for i in range(len(s1)):
            dic[s1[i]] += 1
            if dic[s1[i]] == 0: del dic[s1[i]]
            dic[s2[i]] -= 1
            if dic[s2[i]] == 0: del dic[s2[i]]
        
        # 滑动窗口检查
        i = 0
        for j in range(len(s1), len(s2)):
            if not dic:
                return True  # 如果字典为空，说明s1是s2的排列组合
            
            dic[s2[j]] -= 1
            if dic[s2[j]] == 0: del dic[s2[j]]
            dic[s2[i]] += 1
            if dic[s2[i]] == 0: del dic[s2[i]]
            i += 1
        
        return not dic  # 检查最后的字典是否为空

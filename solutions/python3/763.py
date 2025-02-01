
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # 初始化结果列表来存储分割片段的大小
        sizes = []
        
        # 当字符串S不为空时，继续循环
        while S:
            i = 1
            
            # 寻找使当前子串和剩余部分没有重复字符的最小i值
            while set(S[:i]) & set(S[i:]):
                i += 1
                
            # 将找到的分割点长度加入结果列表
            sizes.append(i)
            
            # 移除已处理的部分，继续处理剩余字符串
            S = S[i:]
        
        # 返回所有分割片段的大小
        return sizes

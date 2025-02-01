    
class Solution:
    # 判断给定字符串 s 是否能使用给定的单词列表 wordDict 中的单词拼接而成

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 初始化右边界列表和单词集合
        rightmosts, words = [0], set(wordDict)
        
        # 遍历字符串 s 的每一个可能的结束位置 i
        for i in range(1, len(s) + 1):
            # 对于当前遍历到的每个位置 i，检查之前所有右边界位置 last_index
            for last_index in rightmosts:
                # 如果子串 s[last_index:i] 在单词集合 words 中，则更新右边界列表，并检查是否已经到达字符串末尾
                if s[last_index:i] in words:
                    rightmosts.append(i)
                    if i == len(s): 
                        return True
                    break
        
        # 遍历结束后，如果未找到满足条件的分割方式，则返回 False
        return False
    
    

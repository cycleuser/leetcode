
from collections import Counter as cnt

# 中文注释：定义一个解决方案类，用于计算在给定字符中能组成的单词长度之和
class Solution:
    # 英文注释: Define a solution class to calculate the sum of lengths of words that can be formed using given characters
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 中文注释：遍历每个单词，判断是否可以用给定字符组成该单词
        # 英文注释: Iterate through each word and check if it can be formed using the given characters
        
        return sum(not cnt(w) - cnt(chars) and len(w) for w in words)

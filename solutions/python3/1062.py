
class Solution:
    # 定义一个类来解决最长重复子串问题

    def longestRepeatingSubstring(self, S: str) -> int:
        # 从字符串的长度开始，逐步减少长度进行搜索
        for length in range(len(S), 0, -1):
            current_substring = S[:length]
            seen_substrings = {current_substring}
            
            # 检查剩余部分中是否存在与当前子串匹配的部分
            for j in range(length, len(S)):
                current_substring = current_substring[1:] + S[j]
                
                if current_substring in seen_substrings:
                    return length
                
                seen_substrings.add(current_substring)
        
        # 如果没有找到重复子串，返回0
        return 0


class Solution:
    # 计算二进制字符串中的连续子字符串数量
    
    def countBinarySubstrings(self, s: str) -> int:
        # 将交替的'01'和'10'替换为'#', 以分割字符串
        s = s.replace("01", "0#1").replace("10", "1#0").split("#")
        
        # 计算相邻子字符串长度的最小值之和作为结果
        return sum(min(len(s[i]), len(s[i - 1])) for i in range(1, len(s)))


class Solution:
    def numDecodings(self, s):
        """
        判断字符串s可以有多少种解码方法。
        
        解码规则：
        - 单个字符 '1'~'9' 可以解码为一个数字（A~I）；
        - 两个字符 '10'~'26' 可以解码为一个字母（J~Z）。

        :param s: str，待解码的字符串
        :return: int，解码方法的数量
        """
        
        if s[0] == "0": 
            return 0  # 如果第一个字符是 '0'，直接返回0
        
        dp1 = dp2 = 1  # 初始化动态规划数组 dp1 和 dp2，dp2 表示当前位的解码数
        
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): 
                return 0  # 如果当前是 '0'，且前一个字符不是 '1' 或 '2' 则无法解码
            
            dp1, dp2 = [dp2, dp1] if s[i] == "0" else [dp2, dp2 + dp1] if "10" <= s[i - 1: i + 1] <= "26" else [dp2, dp2]
        
        return dp2

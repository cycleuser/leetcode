
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        判断字符串s是否匹配模式p。
        
        Parameters:
        s (str): 输入的字符串
        p (str): 匹配模式，其中 '?' 可以匹配任意单个字符， '*' 可以匹配零个或多个任意字符
        
        Returns:
        bool: 如果s匹配p则返回True，否则返回False
        """
        
        sp = pp = match = 0
        star = -1  # 记录'*'的位置
        
        while sp < len(s):
            if (pp < len(p) and (s[sp] == p[pp] or p[pp] == '?')):
                # 当前字符匹配或者当前模式为'?'
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':
                # 当前模式为'*'，记录位置并跳过
                star = pp
                match = sp
                pp += 1
            elif star != -1:
                # 之前的模式中包含'*'
                pp = star + 1
                match += 1
                sp = match
            else:
                return False
        
        while pp < len(p) and p[pp] == '*':
            # 尾部处理，跳过剩余的'*'
            pp += 1
        
        return pp == len(p)

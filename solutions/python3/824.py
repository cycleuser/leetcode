
class Solution:
    def toGoatLatin(self, S):
        """
        将字符串转换为Goat Latin格式。
        
        参数：
            S (str): 输入的原始字符串
        
        返回：
            str: 转换后的Goat Latin格式的字符串
        """
        s, vowels = S.split(), {"a", "e", "i", "o", "u"}  # 分割字符串并定义元音集合
        return " ".join([(s[i][0].lower() in vowels and s[i] or s[i][1:] + s[i][0]) + "ma" + "a" * (i + 2) for i in range(len(s))])  # 生成Goat Latin格式字符串

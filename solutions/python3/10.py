
class Solution:
    """
    判断字符串s是否完全匹配正则表达式模式p。

    中文注释：
    判断字符串s是否完全符合正则表达式模式p的匹配。
    
    :param s: 要匹配的字符串
    :param p: 正则表达式模式
    :return: 如果s完全匹配p，则返回True，否则返回False
    """
    def isMatch(self, s: str, p: str) -> bool:
        # 使用正则表达式的match方法进行匹配
        match_result = re.match(p, s)
        
        # 检查是否匹配成功且整个字符串都被匹配到
        return match_result and match_result.group(0) == s


class Solution:
    """
    解决方案类
    
    Attributes:
        None
    """

    def findTheDifference(self, s: str, t: str) -> str:
        """
        找出字符串t中比字符串s多一个字符的那一个。
        
        参数:
            s (str): 字符串1
            t (str): 字符串2
        
        返回:
            str: 多出来的那个字符
        """
        return next(iter(collections.Counter(t) - collections.Counter(s)))


class Solution:
    # 判断给定的牌组是否可以分成若干个大小相同的小组，且小组的大小大于等于2
    
    def hasGroupsSizeX(self, deck):
        """
        :param deck: List[int] - 牌组列表
        :return: bool - 是否可以分成大小相同的小组
        
        1. 使用collections.Counter计算每个牌的数量
        2. 对这些数量进行辗转相除法求最大公约数（GCD）
        3. 如果最大公约数不等于1，则说明可以分成若干个大小相同的小组，且小组的大小大于等于2
        """
        
        import functools
        from collections import Counter
        
        # 计算每个牌的数量
        counts = Counter(deck).values()
        
        # 使用functools.reduce对所有数量求最大公约数
        gcd_value = functools.reduce(gcd, counts)
        
        # 检查是否可以分成大小相同的小组
        return gcd_value != 1

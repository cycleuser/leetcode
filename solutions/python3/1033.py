
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """
        将三个数排序，方便后续计算移动次数。
        Sort the three numbers for easier calculation of moves.
        """
        a, b, c = sorted([a, b, c])
        
        """
        计算中间位置和c之间的空位数量。
        Calculate the number of empty positions between the middle position and c.
        """
        m1 = b - 1 - a
        
        """
        计算b和c之间的空位数量。
        Calculate the number of empty positions between b and c.
        """
        m2 = c - b - 1

        # 直接计算m1 + m2，因为后续需要这个值。
        _ = m1 + m2
        
        """
        如果a, b间或b, c间只需要一步即可移动，则返回[1, m1 + m2]。
        If a and b or b and c are only one step apart, return [1, m1 + m2].
        """
        if a + 2 == b or b + 2 == c:
            return [1, m1 + m2]
        
        """
        计算b左侧需要移动的次数。
        Calculate the number of moves needed to move stones from left.
        """
        n1 = int(b - 1 > a)
        
        """
        计算b右侧需要移动的次数。
        Calculate the number of moves needed to move stones from right.
        """
        n2 = int(b + 1 < c)
        
        # 返回需要的操作次数
        return [n1 + n2, m1 + m2]

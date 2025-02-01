
class Solution:
    """
    中文注释：该类包含一个方法用于判断给定整数N是否可以通过重排其数字形成2的幂。
    英文注释: This class contains a method to determine if the given integer N can be rearranged to form a power of 2.
    """

    def reorderedPowerOf2(self, N: int) -> bool:
        """
        中文注释：通过计算N和2的幂次方的数字计数是否相同来判断。
        英文注释: Determine if the digit count of N and any power of 2 is the same.
        
        :param N: 给定整数
        :return: 如果可以通过重排其数字形成2的幂则返回True，否则返回False
        """
        cnt = collections.Counter(str(N))
        # 检查N的数字计数是否与2^c的数字计数相同，其中0<=c<32（因为2^31已经是32位整数）
        return any(cnt == collections.Counter(str(1 << c)) for c in range(32))

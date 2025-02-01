
class Solution:
    def isOneBitCharacter(self, bits):
        """
        判断最后一个字符是否为1位字符

        英文注释：
        Determine whether the last character is a 1-bit character.
        """
        while bits:
            # 弹出第一个元素，若为1，则再弹出一个
            first = bits.pop(0)
            if first == 1: 
                bits.pop(0)
        
        # 判断最后一个剩余的字符是否为0
        return last == 0 if len(bits) > 0 else True

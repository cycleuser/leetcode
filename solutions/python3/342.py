
class Solution:
    # 判断给定整数是否是4的幂
    def isPowerOfFour(self, num: int) -> bool:
        # 如果数字小于0，直接返回False
        if num < 0:
            return False
        
        i = 1  # 初始化i为1，因为4的幂至少从1开始
        while i < num:
            # 将i乘以4，在循环中逐步增加i的值
            i *= 4

        # 如果最终i等于num，则说明num是4的幂
        return i == num

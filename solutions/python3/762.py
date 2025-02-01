
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int  # 输入左边界
        :type R: int  # 输入右边界
        :rtype: int    # 返回满足条件的数字个数

        计算区间[L, R]内二进制表示中1的数量为素数的整数个数。
        """
        
        prime_set_bits = {2, 3, 5, 7, 11, 13, 17, 19}  # 素数集合
        count = 0

        while L <= R:
            bit_count_L = bin(L).count('1')  # 计算L的二进制表示中1的数量
            if bit_count_L in prime_set_bits:  # 判断该数量是否为素数
                count += 1
            
            bit_count_R = bin(R).count('1')  # 同上，计算R的二进制表示中1的数量
            if bit_count_R in prime_set_bits:
                count += 1

            L += 1
            R -= 1
        
        return count


class Solution:
    # 定义一个计算从1到n之间数字中包含多少个1的方法
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0  # 如果输入的数小于等于0，返回0

        q, x, ans = n, 1, 0  # 初始化q为n，x为1，ans为0
        while q > 0:  # 当q大于0时循环
            digit = q % 10  # 取当前位的数字
            q //= 10  # 更新q为去掉末尾数后的值

            ans += q * x  # 计算低位中每个位置上1出现的次数

            if digit == 1:
                ans += n % x + 1  # 当前位是1时，加上个位到n的贡献
            elif digit > 1:
                ans += x  # 当前位大于1时，当前位为1的情况要加x次

            x *= 10  # 更新x的值，用于下一位数的计算
        return ans  # 返回结果

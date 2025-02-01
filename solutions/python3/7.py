
class Solution:
    # 定义一个reverse方法，用于反转整数x的位数
    def reverse(self, x: int) -> int:
        # 如果x为正数，则直接反转字符串形式的数字并转换回整数
        if x >= 0:
            reversed_x = int(str(x)[::-1])
        else:
            # 如果x为负数，先反转其绝对值的字符串形式，去掉最后一个字符（原符号），再添加负号
            reversed_x = -int("-" + str(x)[::-1][:-1])

        # 检查反转后的整数值是否在32位有符号整数范围内
        return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0

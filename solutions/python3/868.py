
class Solution:
    # Python类定义

    def binaryGap(self, N):
        """
        :param N: int，输入的整数
        :return: int，二进制表示中最大连续0之间的1的距离
        """
        pre = dist = 0
        for i, c in enumerate(bin(N)[2:]):
            # 遍历N的二进制表示（去掉前缀'0b'），计算每个字符的位置索引i和值c
            if c == "1":
                # 如果当前字符是"1"
                dist = max(dist, i - pre)
                # 计算上一个"1"与当前"1"之间的距离，更新最大距离dist
                pre = i
                # 更新上一个"1"的位置为当前位置i
        return dist
        # 返回计算得到的最大距离

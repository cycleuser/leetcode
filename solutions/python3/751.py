
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        """
        将IP地址转换为二进制形式，处理连续的网络前缀直到分配完n个IP。

        中文注释：将IP地址转换为二进制表示，并计算连续的网络前缀以分配给n个IP。
        """
        s = ''.join(bin(int(num))[2:].zfill(8) for num in ip.split('.'))  # 将IP地址每部分转换为8位二进制字符串
        res = []  # 存储结果列表

        while n:  # 当剩余要分配的IP数量大于0时循环处理
            for i in range(31 - s.rindex('1'), -1, -1):  # 从最右边第一个1开始，向左找连续的网络前缀长度
                if 2 ** i <= n:  # 检查当前网络前缀是否小于剩余要分配的IP数量
                    res.append(
                        '.'.join(str(int(s[i:i + 8], 2)) for i in range(0, 32, 8)) + '/' + str(32 - i)  # 构建CIDR地址并添加到结果列表中
                    )
                    n -= 2 ** i  # 减少剩余要分配的IP数量
                    s = bin(int(s, 2) + 2 ** i)[2:].zfill(32)  # 更新二进制字符串表示，为下一个网络前缀做准备
                    break

        return res


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        """
        给定两个整数 L 和 R ，找到所有在[L,R]区间内的超回文数字。
        
        参数:
            L (str): 区间左边界
            R (str): 区间右边界
        
        返回:
            int: 在[L,R]区间内的超回文数字个数
        """
        from math import floor, ceil

        # 将输入转换为整数
        L, R = int(L), int(R)

        # 计算左右边界的平方根并取整
        left_sqrt = int(floor(math.sqrt(L)))
        right_sqrt = int(ceil(math.sqrt(R)))

        # 获取平方根的字符串长度，并根据奇偶性计算回文中心长度
        n1, n2 = len(str(left_sqrt)), len(str(right_sqrt))
        n1 = (n1 // 2) if n1 % 2 == 0 else (n1 // 2 + 1)
        n2 = (n2 // 2) if n2 % 2 == 0 else (n2 // 2 + 1)

        # 计算回文范围的起始和结束值
        start = int('1' + '0' * (n1 - 1))
        end = int('9' * n2) + 1

        ans = 0
        for i in range(start, end):
            x = str(i)
            # 构建回文数：x + 反转(x)
            num1 = int(x + x[::-1])
            # 特殊情况处理：x + 去掉末位的反转(x) (适用于奇数长度的情况)
            num2 = int(x + x[:-1][::-1]) if len(x) % 2 == 1 else 0

            for num in [num1, num2]:
                # 检查生成的回文平方是否在[L,R]区间内且是超回文
                cand = num * num
                if L <= cand <= R and str(cand) == str(cand)[::-1]:
                    ans += 1

        return ans

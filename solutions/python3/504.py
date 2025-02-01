
class Solution:
    # 将整数转换为7进制表示
    def convertToBase7(self, num: int) -> str:
        # 如果num大于0，前导字符串为空；等于0时设为"0"；小于0时添加负号
        lead = "" if num > 0 else "0" if num == 0 else "-"
        
        res, num = [], abs(num)
        # 当num不为0时循环，每次取模7并整除7
        while num:
            res.append(int(num % 7))
            num //= 7
        
        # 反转结果列表，并转换成字符串拼接返回
        return lead + "".join(str(c) for c in res[::-1])

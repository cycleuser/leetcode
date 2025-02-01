
class Solution:
    def toHex(self, num: int) -> str:
        """
        将给定的整数转换为16进制字符串。
        
        参数:
            num (int): 需要转换的整数值
        
        返回:
            str: 转换后的16进制字符串
        """
        if not num: 
            return "0"
        
        # 用于映射16进制字符
        mp = "0123456789abcdef"
        ans = ""
        
        # 处理最多8次循环，因为int型整数至少可以表示为8个16进制位
        for i in range(8):
            n = num & 15  # 取最低四位进行转换
            c = mp[n]     # 获取对应的十六进制字符
            ans = c + ans # 将当前字符加入结果字符串的开头
            num >>= 4    # 向右移动4位，处理下一位
        
        return ans.lstrip('0')  # 移除前导零

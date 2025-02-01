
class Solution:
    # 将罗马数字转换为整数
    
    def romanToInt(self, s):
        # 创建一个字典用于存储罗马数字与其对应整数值的映射
        table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        
        # 初始化结果和前一个字符，默认为'I'，表示初始值
        sm, pre = 0, 'I'
        
        # 反向遍历字符串s中的每一个字符c
        for c in s[::-1]:
            # 如果当前字符对应的数值小于前一个字符的数值，则减去当前字符对应的整数值
            if table[c] < table[pre]:
                sm, pre = sm - table[c], c  
            else:
                # 否则，加上当前字符对应的整数值，并更新前一个字符为当前字符
                sm, pre = sm + table[c], c
        
        return sm  # 返回最终的结果

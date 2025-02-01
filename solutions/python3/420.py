
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # 计算缺失的类型数量
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): 
            missing_type -= 1  # 检查小写字母
        if any('A' <= c <= 'Z' for c in s): 
            missing_type -= 1  # 检查大写字母
        if any(c.isdigit() for c in s): 
            missing_type -= 1  # 检查数字

        change = 0  # 需要改变的操作数
        one = two = 0  # len=3, len=2的重复字符数量
        p = 2  # 开始检查从索引2开始
        
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:  # 检查三个连续相同字符
                length = 2  # 初始化重复长度为2
                while p < len(s) and s[p] == s[p-1]:
                    length += 1  # 增加重复长度
                    p += 1
                    
                change += length // 3  # 计算需要的操作数
                if length % 3 == 0: 
                    one += 1  # 长度为3的重复序列数量+1
                elif length % 3 == 1: 
                    two += 1  # 长度为2的余1的重复序列数量+1
            else:
                p += 1  # 移动指针
        
        # 根据字符串长度计算需要的操作数
        if len(s) < 6: 
            return max(missing_type, 6 - len(s))  # 字符串太短，返回缺失类型或补足长度的最大值
        elif len(s) <= 20: 
            return max(missing_type, change)  # 长度在合理范围内，返回缺失类型或改变操作数的最大值
        else:
            delete = len(s) - 20  # 计算删除的字符数量
            
            change -= min(delete, one)  # 尽量删除重复序列中的一个3长度
            change -= min(max(delete - one, 0), two * 2) // 2  # 删除两个长度为2的重复序列，但优先处理余1的情况
            change -= max(delete - one - 2 * two, 0) // 3  # 删除单个字符来优化剩余的操作数
            
            return delete + max(missing_type, change)  # 返回删除操作和最终改变操作的最大值


class Solution:
    # 定义一个解决方案类
    
    def crackSafe(self, n: int, k: int) -> str:
        # n：字符串的长度，k：每个位置上的字符数
        
        s = '0' * (n - 1)
        # 初始化字符串s为n-1个'0'
        
        D = '9876543210'[-k:]
        # 获取用于构建组合的字符集合D
        # 通过切片获取长度为k的数字字符
        
        for _ in range(k**n):
            # 遍历所有可能的组合数，即k^n次
            next_d = next(d for d in D if (s + d)[-n:] not in s)
            # 选择一个未出现过的子串d作为下一个字符
            
            s += next_d
            # 将选择的字符添加到字符串s中
        
        return s
        # 返回最终构建的字符串s


class Solution:
    # 定义一个类来解决字符串相关的问题

    def lastSubstring(self, s: str) -> str:
        # 初始化结果变量，用于存储最长子串
        result = ""
        
        # 遍历字符串的每一个字符作为起始位置
        for i in range(len(s)):
            # 从当前索引i开始，获取后续的所有子串，并与result进行比较取最大值
            result = max(result, s[i:])
        
        # 返回最终找到的最大子串
        return result

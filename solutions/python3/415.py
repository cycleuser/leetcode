
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        :type num1: str  # 字符串num1
        :type num2: str  # 字符串num2
        :rtype: str      # 返回相加后的字符串结果
        """
        # 计算num1的数值并累加到result中
        result = sum((ord(num1[i]) - ord('0')) * (10 ** (len(num1) - 1 - i)) for i in range(len(num1)))
        
        # 计算num2的数值并累加到result中
        result += sum((ord(num2[i]) - ord('0')) * (10 ** (len(num2) - 1 - i)) for i in range(len(num2)))
        
        # 将最终结果转换为字符串并返回
        return str(result)

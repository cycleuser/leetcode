
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        """
        检查字符串S中是否包含从1到N的所有二进制表示
        
        Chinese:
        检查字符串S中是否存在从1到N的所有二进制表示形式。
        
        参数:
            S (str): 输入的字符串
            N (int): 需要检查的最大整数
        
        返回:
            bool: 如果S包含所有从1到N的二进制表示，则返回True，否则返回False
        """
        # 使用集合进行差集计算，找出缺失的二进制值
        return not set(range(1, N + 1)) - {int(S[i:j + 1], 2) for i in range(len(S)) for j in range(i, len(S))}

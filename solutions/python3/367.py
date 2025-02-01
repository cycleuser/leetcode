
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int  # 输入的整数 num
        :rtype: bool     # 返回是否是完全平方数
        """
        i = 1  # 初始化搜索起点为1
        
        # 使用二分查找优化循环，减少不必要的计算
        while i**2 <= num:
            if i**2 < num:
                i += 1
            elif i**2 == num: 
                return True  # 找到完全平方数，返回True
        
        return False  # 循环结束仍未找到，返回False

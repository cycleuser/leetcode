
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 使用集合记录已经出现过的数字，避免重复计算
        # Use a set to record numbers that have appeared to avoid redundant calculations
        mem = set()
        
        while n != 1:
            # 将当前数字转换为字符串，并计算每个字符的平方和
            # Convert the current number to string and calculate the sum of squares of each character
            n = sum([int(i) ** 2 for i in str(n)])
            
            if n in mem: 
                return False
            else:
                mem.add(n)
        else:
            return True


class Solution:
    def findMaximumXOR(self, nums, ans=0):
        """
        寻找给定数组中的最大异或值。
        
        Args:
            nums (List[int]): 输入整数列表。
            ans (int): 累计结果，默认为0。
        
        Returns:
            int: 给定数组中任意两个数的最大异或值。
        """
        ans = 0
        for bit in range(30, -1, -1):
            # 将当前的ans左移一位，相当于在二进制表示中增加一个0
            ans <<= 1
            
            # 尝试将当前位设置为1，并记录是否可以形成最大异或值
            attempt = ans | 1
            
            # 使用集合存储前缀值
            prefix = set()
            
            for x in nums:
                # 计算当前x在第bit位的前缀值
                p = x >> bit
                
                # 如果存在一个之前出现过的前缀，与尝试的值异或后等于ans，则更新最大结果
                if attempt ^ p in prefix:
                    ans = attempt
                    break
                
                # 将当前前缀添加到集合中
                prefix.add(p)
        
        return ans

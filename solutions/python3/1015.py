
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        """
        解决问题：给定一个整数 K，找到最短的由 1 组成且能被 K 整除的连续子序列长度。
        
        中文注释：
        - 目标是找到最短的全由 1 构成的子串，使其能被 K 整除
        """
        used, mod, cnt = set(), 1 % K, 1  # 初始化已使用过的模值集合、当前余数和计数器
        
        while mod:  # 当余数不为0时循环
            mod = (mod * 10 + 1) % K  # 计算新的余数，相当于将当前序列长度增加1并取模K
            cnt += 1  # 增加计数器
            
            if mod in used:  # 如果当前余数已经出现过，说明形成循环，无解
                return -1
            used.add(mod)  # 将当前余数加入已使用集合
        
        return cnt  # 返回最短子序列长度

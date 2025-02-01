
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        """
        判断给定整数列表A中每个前缀（包括整个序列）是否能被5整除。
        
        Args:
            A (List[int]): 输入的整数列表
        
        Returns:
            List[bool]: 每个前缀能否被5整除的结果列表
        """
        num = 0  # 初始化当前数值为0
        for i in range(len(A)):
            # 将当前位加入到num中，并更新num，同时判断前i+1位是否能被5整除
            num = (num << 1) + A[i]
            A[i] = num % 5 == 0  # 更新结果列表中的当前值
        return A  # 返回最终的结果列表

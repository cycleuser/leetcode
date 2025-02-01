
class Solution:
    def fairCandySwap(self, A: list[int], B: list[int]) -> list[int]:
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        # 将列表A和B转换为集合，以提高查找效率
        a, b = set(A), set(B)
        
        # 计算双方糖果数量差值的一半
        diff = (sum(A) - sum(B)) // 2
        
        # 遍历集合B中的每一个元素c
        for c in B:
            # 检查c加上计算出的差值是否在集合A中，以找到公平交换的糖果组合
            if c + diff in a:
                return [c + diff, c]

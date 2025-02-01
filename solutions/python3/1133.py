
class Solution:
    # 定义一个类来解决寻找数组中最大唯一数字的问题

    def largestUniqueNumber(self, A: List[int]) -> int:
        # 使用Counter计算每个元素的出现次数
        cnt = collections.Counter(A)
        
        # 找出所有只出现一次的元素，并进行排序
        a = sorted(k for k, v in cnt.items() if v == 1)
        
        # 如果有符合条件的元素，返回最大的那个；否则返回-1
        return a[-1] if a else -1

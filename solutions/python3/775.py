
class Solution:
    # 判断给定数组是否为理想排列，即每个元素与它的索引差的绝对值不超过1
    def isIdealPermutation(self, A):
        # 遍历数组中的每一个元素及其索引
        for i, num in enumerate(A):
            # 检查当前元素与索引的差异是否在-1到1之间，否则返回False
            if not (i - 1 <= num <= i + 1): 
                return False
        # 如果所有检查都通过，则返回True
        return True

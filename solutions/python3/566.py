    
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        :param nums: 二维整数列表
        :param r: 期望重塑后的矩阵行数
        :param c: 期望重塑后的矩阵列数
        :return: 如果可以重塑，返回重塑后的矩阵；否则返回原矩阵
        """

        # 将原始二维数组展平为一维列表
        nums_ordered = [x for y in nums for x in y]

        # 判断是否可以进行重塑操作
        if r * c == len(nums) * len(nums[0]):
            # 可以重塑，按要求分割并重组为新的矩阵
            return [nums_ordered[c * i:c * (i + 1)] for i in range(r)]
        else:
            # 无法重塑，返回原矩阵
            return nums
    

class Solution:
    # 定义一个类来解决排序问题

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        使用快速排序算法对整数列表进行排序。

        参数:
            nums (List[int]): 需要排序的整数列表
        
        返回:
            List[int]: 排序后的整数列表
        """

        if len(nums) <= 1:
            # 如果数组长度小于等于1，直接返回该数组
            return nums

        pivot = random.choice(nums)
        # 选择一个枢轴元素
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]
        # 根据枢轴将数组分为小于、等于和大于三部分

        return self.sortArray(lt) + eq + self.sortArray(gt)
        # 递归排序小于部分，等于部分直接加入结果，再递归排序大于部分

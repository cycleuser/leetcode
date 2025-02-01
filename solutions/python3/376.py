
class Solution:
    def wiggleMaxLength(self, nums):
        """
        :param nums: List[int] 输入的整数列表
        :return: int 返回最长摆动子序列长度

        中文注释：
        - 检查输入长度小于等于2时的情况
        - 初始化上升标志和计数值
        - 遍历数组，根据条件更新上升标志并增加计数值
        """
        # 如果输入列表长度小于或等于2直接返回结果
        if len(nums) <= 2:
            return 0 if not nums else 1 if nums[0] == nums[-1] else 2

        # 初始化比较上一个元素和当前元素是否上升的标志，和初始计数值
        inc = None if nums[0] != nums[1] else None
        cnt = 2 if inc is not None else 1

        # 遍历数组从第三个元素开始
        for i in range(2, len(nums)):
            # 如果当前元素与前一个元素不同且上升标志未定义或状态改变
            if nums[i - 1] != nums[i] and (inc is None or inc != (nums[i - 1] < nums[i])):
                # 更新上升标志并增加计数值
                inc = nums[i - 1] < nums[i]
                cnt += 1

        return cnt


class Solution:
    # 定义一个移除数组中重复元素的方法，返回去重后数组的新长度
    def removeDuplicates(self, nums):
        n = len(nums)
        # 遍历数组，从倒数第二个元素开始向前检查相邻两个元素是否相等
        # 如果相等，则删除该元素，并调整后续元素的位置
        [nums.pop(i) for i in range(n - 1, 0, -1) if nums[i] == nums[i - 1]]
        return n - len(nums)



class Solution:
    # 定义一个移除数组中重复元素的方法，返回去重后数组的新长度
    def removeDuplicates(self, nums):
        n = len(nums)
        # 使用列表推导式逆向遍历并删除相邻相等的元素
        [nums.pop(i) for i in range(n - 1, 0, -1) if nums[i] == nums[i - 1]]
        return n - len(nums)

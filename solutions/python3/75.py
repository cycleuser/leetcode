
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]   # 输入参数为一个整数列表
        :rtype: void            # 不返回任何值，而是就地修改 nums 列表
        """
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                # 遇到 0，则交换 red 和 white 指向的元素，并各自右移一位
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                # 遇到 1，则仅将 white 右移一位，不做交换操作
                white += 1
            else:
                # 遇到 2，则交换 blue 和 white 指向的元素，并将 blue 左移一位
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

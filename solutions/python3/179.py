
class Solution:
    # 定义快速排序的分区函数，用于比较两个数拼接后的大小
    def partition(self, l: int, r: int):
        j = l
        for i in range(l + 1, r + 1):
            if nums[i] + nums[l] >= nums[l] + nums[i]:
                # 如果num[i]+nums[l] >= nums[l]+num[i]，则交换位置
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        # 最后将分界点与第一个元素交换
        nums[l], nums[j] = nums[j], nums[l]
        return j

    # 定义快速排序函数
    def quickSort(self, l: int, r: int):
        if l < r:
            m = self.partition(l, r)
            self.quickSort(l, m - 1)
            self.quickSort(m + 1, r)

    # 将数字转换为字符串数组，并进行排序
    nums = [str(num) for num in nums]
    quickSort(0, len(nums) - 1)

    # 合并成一个数，去掉前导零，返回结果
    return str(int("".join(nums)))

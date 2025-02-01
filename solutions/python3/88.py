
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        :param nums1: 第一个数组，其中前m个元素有效
        :param m: 第一个数组的有效长度
        :param nums2: 第二个数组
        :param n: 第二个数组的长度
        :return: 无返回值，直接修改nums1
        """
        # 使用双指针从后向前比较和填充元素
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # 将剩余的nums2元素填充到nums1中
        if n > 0:
            nums1[:n] = nums2[:n]

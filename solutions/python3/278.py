
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    """
    :type n: int       # 输入整数n，表示要检查的版本号范围的最大值
    :rtype: int        # 返回第一个坏版本的版本号
    """
    def firstBadVersion(self, n):
        """
        二分查找法寻找第一个出现错误的版本号

        :param n: 要检查的版本号范围的最大值
        :return: 第一个坏版本的版本号
        """
        l, r = 0, n  # 初始化左右指针
        while l <= r:
            mid = (l + r) // 2  # 计算中间位置
            if isBadVersion(mid):  # 如果当前mid是坏版本
                r = mid - 1  # 将右边界调整到mid左边，继续在左半部分查找
            else:  # 否则，当前mid不是坏版本
                l = mid + 1  # 将左边界调整到mid右边，继续在右半部分查找
        return r + 1  # 最后返回的r是最后一个未出现错误的版本号，所以返回r+1即为第一个坏版本号

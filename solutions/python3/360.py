
class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        对给定的数组进行变换并排序。

        参数:
            nums (List[int]): 输入的整数列表。
            a, b, c (int): 二次多项式系数，用于对每个元素进行变换: ax^2 + bx + c。

        返回:
            List[int]: 变换后的数组，并按升序排列。
        """
        arr, l, r, ind = [0] * len(nums), 0, len(nums) - 1, a >= 0 and len(nums) - 1 or 0
        # 使用双指针法，分别指向列表的起始和末尾
        while l <= r:
            n1 = a * nums[l] * nums[l] + b * nums[l] + c  # 计算左指针对应位置的值
            n2 = a * nums[r] * nums[r] + b * nums[r] + c  # 计算右指针对应位置的值
            
            if a >= 0:  # 当a>=0时，开口向上
                if n1 >= n2:
                    arr[ind] = n1  # 将较大的数填入结果数组
                    l += 1
                else:
                    arr[ind] = n2
                    r -= 1
                ind -= 1  # 索引从后向前填写
            else:  # 当a<0时，开口向下
                if n1 < n2:
                    arr[ind] = n1
                    l += 1
                else:
                    arr[ind] = n2
                    r -= 1
                ind += 1  # 索引从前向后填写
        
        return arr

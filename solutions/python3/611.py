
class Solution:
    # 定义一个求三角形个数的类

    def triangleNumber(self, nums):
        """
        :param nums: List[int] -- 输入的一组整数数组
        :return: int -- 满足条件的三角形个数
        """
        res, n = 0, len(nums)  # 初始化结果和数组长度
        nums.sort()  # 对输入数组进行排序，便于后续操作
        
        for i in range(n - 1, 1, -1):  # 从右向左遍历，减少不必要的计算
            j, k = i - 1, 0  # 定义双指针j和k，初始值分别为i-1和0
            
            while k < j:  # 当j > k时继续循环
                if nums[j] + nums[k] > nums[i]:  # 判断是否能构成三角形
                    res += (j - k)  # 满足条件则计算个数并累加到结果中
                    j -= 1  # 更新指针位置
                else:
                    k += 1  # 移动左指针，寻找可能的组合
        
        return res  # 返回最终结果

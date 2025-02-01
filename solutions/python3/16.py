
class Solution:
    # 定义一个类，用于解决寻找最接近目标值的三个数之和的问题
    
    def threeSumClosest(self, nums, target):
        """
        :param nums: List[int] - 一个整数数组
        :param target: int - 目标整数值
        :return: int - 三个元素之和最接近目标值的和
        """
        
        res = diff = float("inf")  # 初始化结果变量res和差值diff为无穷大
        nums.sort()  # 对数组进行排序，便于后续操作
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue  # 跳过重复的元素
            
            l, r = i + 1, len(nums) - 1  # 定义左右指针
            while l < r:
                sm = nums[i] + nums[l] + nums[r]  # 计算三个数之和
                
                if abs(sm - target) < diff: 
                    diff, res = abs(sm - target), sm  # 更新最小差值及其对应的三数之和
                
                if sm < target:
                    l += 1  # 如果当前和小于目标，则移动左指针
                elif sm > target:
                    r -= 1  # 如果当前和大于目标，则移动右指针
                else:
                    return res  # 如果找到等于目标的三数之和，直接返回
        
        return res  # 返回最接近目标值的三个数之和

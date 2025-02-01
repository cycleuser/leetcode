
class Solution:
    def threeSum(self, nums):
        """
        给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a, b, c ，使得 a + b + c = 0？
        如果存在，请返回任意一个满足条件三元组；否则返回空列表。
        
        :param nums: List[int] - 需要处理的整数列表
        :return: List[List[int]] - 所有和为0的三个元素组成的数组，每个元素是一个包含3个int的数组
        """
        res, res_set = [], set()
        # 对数组进行排序以简化后续判断逻辑
        nums.sort()
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm < 0: 
                    # 当三数之和小于0，移动左指针使总和变大
                    l += 1
                elif sm > 0: 
                    # 当三数之和大于0，移动右指针使总和减小
                    r -= 1
                else:
                    # 找到一个符合条件的组合，加入结果集并去重
                    if (nums[i], nums[l], nums[r]) not in res_set: 
                        res.append([nums[i], nums[l], nums[r]])
                        res_set.add((nums[i], nums[l], nums[r]))
                    
                    l, r = l + 1, r - 1  # 移动指针继续查找下一个可能的组合
        
        return res

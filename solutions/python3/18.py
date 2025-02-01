
class Solution:
    # 定义一个类来解决四数之和问题

    def fourSum(self, nums, target):
        """
        :param nums: 列表，包含整数
        :param target: 目标值
        :return: 返回所有满足条件的四元组列表
        """
        res, res_set = [], set()
        # 初始化结果列表和一个集合用于去重
        
        nums.sort()  # 对输入列表进行排序以简化后续操作

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]: continue
            # 跳过重复元素，避免结果重复
            
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                # 设置双指针初始位置
                
                while l < r:
                    sm = nums[i] + nums[j] + nums[l] + nums[r]
                    # 计算当前四数之和
                    
                    if sm < target: 
                        l += 1
                    elif sm > target: 
                        r -= 1
                    else: 
                        if (nums[i], nums[j], nums[l], nums[r]) not in res_set:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            res_set.add((nums[i], nums[j], nums[l], nums[r]))
                        # 如果当前四数之和等于目标值且未在结果集中，则加入结果集
                        l, r = l + 1, r - 1
        return res  # 返回最终的结果列表

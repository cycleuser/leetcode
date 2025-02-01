
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int  # k 表示组合中数字的数量
        :type n: int  # n 表示目标和
        :rtype: List[List[int]]  # 返回满足条件的组合列表
        """
        stack, nums, res = [(0, [], 0, k)], range(1, 10), []
        
        while stack:
            sm, tmp, index, k_val = stack.pop(0)
            
            for i in range(index, len(nums)):
                if sm + nums[i] < n and k_val > 0: 
                    # 如果当前和小于目标值且剩余组合数大于0，将新状态加入栈中
                    stack.append((sm + nums[i], tmp + [nums[i]], i + 1, k_val - 1))
                elif sm + nums[i] == n and k_val == 1: 
                    # 如果当前和等于目标值且剩余组合数为1，将该组合加入结果列表
                    res.append(tmp + [nums[i]])
        
        return res

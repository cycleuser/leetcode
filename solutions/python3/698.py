
class Solution:
    # 判断是否可以将数组分割为k个具有相同总和的子集
    
    def canPartitionKSubsets(self, nums, k):
        # 深度优先搜索函数，i表示当前处理的数字索引，sums记录每个子集的当前和
        def dfs(i, sums):
            if i == n:  # 所有数字都已分配完毕
                return True
            
            for j in range(k):  # 尝试将当前数字加入k个子集中任一个
                if sums[j] + nums[i] <= target:  # 当前子集和加上该数不超过目标值
                    sums[j] += nums[i]
                    
                    # 继续递归处理下一个数字
                    if dfs(i + 1, sums):
                        return True
                    
                    # 回溯，撤销当前分配决策
                    sums[j] -= nums[i]
            
            return False
        
        # 按降序排序数组，便于后续剪枝
        nums.sort(reverse=True)
        
        # 计算数组总和
        sm = sum(nums)
        
        # 如果总数不能被k整除，则不可能分割成功
        if sm % k: 
            return False
        
        # 目标子集的和与数字个数
        target, n = sm // k, len(nums)
        
        # 从第一个数字开始进行深度优先搜索
        return dfs(0, [0] * k)

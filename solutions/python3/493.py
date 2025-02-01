
class Solution:
    # 初始化结果列表，用于存储最终的逆序对个数
    def reversePairs(self, nums: List[int]) -> int:
        res = [0]
        
        # 合并排序，并统计逆序对数量
        def merge(nums):
            if len(nums) <= 1: 
                return nums
            
            # 分治法，递归拆分数组
            left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            
            for r in right:
                # 计算逆序对数量
                add = len(left) - bisect.bisect_left(left, 2 * r)
                if not add: 
                    break
                
                res[0] += add
            
            return sorted(left + right)
        
        merge(nums)
        return res[0]


class Solution:
    # 初始化结果列表，用于存储最终的逆序对个数
    def reversePairs(self, nums: List[int]) -> int:
        res = [0]
        
        # 合并排序，并统计逆序对数量
        def merge(nums):
            if len(nums) <= 1: 
                return nums
            
            # 分治法，递归拆分数组
            left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            
            for r in right:
                # 计算逆序对数量
                add = len(left) - bisect.bisect_left(left, 2 * r)
                if not add: 
                    break
                
                res[0] += add
            
            return sorted(left + right)
        
        merge(nums)
        return res[0]

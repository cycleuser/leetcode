
class Solution:
    def minPatches(self, nums, n):
        """
        :param nums: List[int] - 可选补丁数组
        :param n: int - 目标最大值
        :return: int - 最小需要添加的补丁数量
        """
        
        miss, added, i = 1, 0, 0
        
        # 当缺失值小于等于目标值时，继续循环
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # 如果当前数字可以覆盖到miss，则更新miss，并移动索引i
                miss += nums[i]
                i += 1
            else:
                # 否则将miss加倍，表示需要添加一个补丁来覆盖该范围
                miss *= 2
                added += 1
        
        return added

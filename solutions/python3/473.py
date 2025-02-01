
class Solution:
    def makesquare(self, nums):
        """
        判断给定的数字列表是否可以构成一个正方形，每个边上的和相同。

        参数:
        nums (List[int]): 数字列表

        返回值:
        bool: 如果可以构成正方形则返回 True，否则返回 False
        """

        def dfs(index, edge, count, used):
            """
            深度优先搜索辅助函数。

            参数:
            index (int): 当前考虑的数字索引
            edge (int): 边长剩余值
            count (int): 已完成的边数
            used (Set[int]): 已使用的数字索引集合
            """
            for i in range(index, len(nums)):
                if i in used or edge - nums[i] < 0: 
                    continue
                elif edge - nums[i] > 0 and dfs(i + 1, edge - nums[i], count, used | {i}): 
                    return True
                elif edge - nums[i] == 0 and (count and dfs(1, l, count - 1, used | {i})) or not count: 
                    return True
            return False

        # 计算数字列表总和
        sm = sum(nums)
        
        # 判断边界条件
        if len(nums) < 4 or sm % 4 != 0:
            return False
        
        # 每条边的目标长度
        l = sm // 4 
        
        # 对数字按降序排序，便于后续剪枝操作
        nums.sort(reverse=True)
        
        # 如果最大值大于目标边长，则无法构成正方形
        if nums[0] > l: 
            return False
        
        # 尝试从第一个元素开始构建每条边
        return nums[0] == l and dfs(1, l, 1, {0}) or dfs(1, l - nums[0], 2, {0})

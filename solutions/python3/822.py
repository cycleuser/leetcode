
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        :param fronts: 正面数字列表
        :param backs: 反面数字列表
        :return: 能翻转的最小不同数字，如果找不到返回0
        """
        # 使用集合操作合并正面和反面数字，并移除同时出现在正面和反面的数字
        unique_numbers = (set(fronts) | set(backs)) - set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i])
        
        # 返回最小值，如果为空则返回0
        return min(unique_numbers, default=0)


class Solution:
    """
    Combination Sum II

    组合总和II

    Given a collection of candidate numbers (candidates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.

    假设给定一个候选数列表（candidates）和目标值（target），找到所有满足条件的唯一组合，
    使候选数之和等于目标值。每个数字只能在组合中使用一次。
    """

    def combinationSum2(self, candidates, target):
        """
        :param candidates: List[int] - 候选数列表
        :param target: int - 目标值
        :return: List[List[int]] - 所有满足条件的唯一组合
        """
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        """
        :param nums: List[int] - 排序后的候选数列表
        :param target: int - 当前目标值
        :param index: int - 起始索引
        :param path: List[int] - 当前路径（组合）
        :param res: List[List[int]] - 结果集
        """
        if target < 0:
            return
        if target == 0 and path not in res:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], target - nums[i], i, path + [nums[i]], res)

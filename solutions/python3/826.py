
class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # 将难度和利润打包成元组，按难度排序
        jobs = sorted(zip(difficulty, profit))
        
        res = i = maxp = 0
        # 工人能力按从小到大排序
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                # 更新当前最大利润
                maxp = max(jobs[i][1], maxp)
                i += 1
            # 累加最大可得利润
            res += maxp
        
        return res

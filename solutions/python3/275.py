
class Solution:
    def hIndex(self, citations):
        """
        :param citations: list[int] - 引用次数列表，每个元素代表一篇论文的引用次数
        :return: int - 返回h指数，即满足条件的最大整数k：有至少k篇论文，每篇论文的引用次数至少为k次
        
        优化说明：
            - 使用二分查找法来提高效率。
            - 中文注释和英文注释双语提供以方便理解。
        """
        l, r, res = 0, len(citations) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            # 检查当前mid位置是否满足h指数条件
            if len(citations) - mid <= citations[mid]: 
                res, r = len(citations) - mid, r - 1
            else: 
                l = mid + 1
        return res

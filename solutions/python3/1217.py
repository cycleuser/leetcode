
class Solution:
    # 计算将所有筹码移动到同一位置所需的最小成本

    def minCostToMoveChips(self, chips: List[int]) -> int:
        # 遍历每个可能的目标位置c1，计算将其余筹码移动到该位置所需的成本
        return min(sum((c1 - c2) % 2 for c2 in chips) for c1 in chips)



class Solution:
    # 计算将所有筹码移动到同一位置所需的最小成本

    def minCostToMoveChips(self, chips: List[int]) -> int:
        # 使用更简洁的逻辑计算所需成本，优化代码结构和性能
        odd_count = sum(1 for chip in chips if chip % 2)
        even_count = len(chips) - odd_count
        return min(odd_count, even_count)

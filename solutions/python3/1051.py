
class Solution:
    # 计算期望高度与实际高度不匹配的儿童数量

    def heightChecker(self, heights: List[int]) -> int:
        # 使用生成器表达式，比较原始高度和排序后高度的差异，并求和
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

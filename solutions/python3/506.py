
class Solution:
    # 定义一个方法来找到相对排名
    def findRelativeRanks(self, nums):
        # 创建一个字典，键为排序后的分数值，值为相应的排名
        rank = {n: i > 2 and str(i + 1) or ["Gold", "Silver", "Bronze"][i] + ' Medal' for i, n in enumerate(sorted(nums, reverse=True))}
        
        # 根据原始输入的分数列表返回对应的排名
        return [rank[num] for num in nums]

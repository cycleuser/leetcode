
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # 计算唯一糖果种类数
        unique_candies = len(set(candies))
        
        # 如果唯一糖果种类数小于等于总糖果数量的一半，则返回唯一糖果种类数，否则返回总糖果数量一半
        return unique_candies if unique_candies <= len(candies) // 2 else len(candies) // 2

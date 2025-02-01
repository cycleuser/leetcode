
class Solution:
    # 分糖果给指定人数，返回每个人的糖果数量列表
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # 初始化每个小孩的糖果数为0
        res = [0] * num_people
        
        i = 0
        # 当剩余糖果大于0时继续分配
        while candies > 0:
            # 分配当前能拿的最大数量的糖果
            res[i % num_people] += min(candies, i + 1)
            # 更新索引i，表示下一个小孩
            i += 1
            # 减少剩余糖果数
            candies -= (i if candies >= i else candies)
        
        return res

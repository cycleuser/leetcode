
class Solution:
    # 定义一个类来解决饮食计划表现问题

    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # 初始化滑动窗口的总热量和初始得分
        sm = sum(calories[:k])
        points = (sm > upper) - (sm < lower)
        
        # 遍历剩余的天数，更新滑动窗口内的总热量并计算得分变化
        for i in range(k, len(calories)):
            sm += calories[i] - calories[i - k]
            points += (sm > upper) - (sm < lower)
            
        return points  # 返回最终的得分



class Solution:
    # 定义一个类来解决饮食计划表现问题

    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        sm = sum(calories[:k])
        points = (sm > upper) - (sm < lower)
        
        for i in range(k, len(calories)):
            sm += calories[i] - calories[i - k]
            points += (sm > upper) - (sm < lower)
            
        return points


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        # 计算初始窗口内的满足顾客数量
        dif = mx = sum(c * g for c, g in zip(customers[:x], grumpy[:x]))
        
        # 遍历剩余的grumpy数组，更新最大差值和滑动窗口
        for j in range(x, len(grumpy)):
            dif += (grumpy[j] * customers[j]) - (grumpy[j - x] * customers[j - x])
            mx = max(mx, dif)
        
        # 返回初始满足顾客数量与非愤怒时段的满足顾客数量之和
        return mx + sum(c * (1- g) for c, g in zip(customers, grumpy))

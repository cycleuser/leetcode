
class Solution:
    # 定义一个解决方案类

    def nthPersonGetsNthSeat(self, n: int) -> float:
        # 返回最大值，这个值要么是0.5（当n非常大时），要么是1/n的倒数
        return max(0.5, 1 / n)
        # 中文注释：返回一个值，该值为0.5和1/n中的较大者。当n增大时，1/n趋近于0，因此返回值接近0.5。


class Solution:
    def lastRemaining(self, n):
        """
        :param n: 整数，表示初始数量 (n)
        :return: 返回第 n 次操作后剩下的最后一个元素的位置
        
        使用数学方法模拟筛选过程，优化空间和时间复杂度。
        """
        head, left, step, remaining = 1, 1, 1, n
        # 当剩余元素大于1时继续循环
        while remaining > 1:
            if left or remaining % 2: 
                # 如果left为True或剩余元素个数为奇数，则前进step步
                head += step
            
            # 每次操作后更新left状态，即下一次筛选方向
            left = 1 - left
            # 更新步长，每次循环步长翻倍
            step *= 2
            # 剩余元素数量减半
            remaining //= 2
        
        return head

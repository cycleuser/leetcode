    
class Solution:
    # 定义一个整数分割问题的解决方案类

    def integerBreak(self, n: int) -> int:
        # 初始化一个列表pre，用于存储n小于7时的结果
        pre = [0, 1, 1, 2, 4, 6, 9]
        
        if n < 7:
            # 如果输入的整数n小于7，直接返回预计算的结果
            return pre[n]

        for i in range(7, n + 1):
            # 对于大于等于7的n值，通过动态规划的方式填充列表pre
            pre.append(max(pre[i - 2] * 2, pre[i - 3] * 3))
        
        # 返回最终的结果
        return pre[-1]
    
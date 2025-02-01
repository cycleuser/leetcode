
class Solution:
    # 定义一个类，用于解决从叶子节点值的最小乘积问题

    def mctFromLeafValues(self, A: List[int]) -> int:
        # 初始化结果变量res为0，数组A长度为n
        res, n = 0, len(A)
        
        # 使用一个栈来辅助计算
        stack = [float('inf')]
        
        # 遍历输入数组A中的每个元素a
        for a in A:
            # 当栈顶元素小于当前元素时，进行弹出操作并累加乘积到结果中
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            
            # 将当前元素压入栈中
            stack.append(a)

        # 当栈中剩余两个以上元素时，继续计算乘积并累加到结果中
        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res  # 返回最终的结果


class Solution:
    # 定义一个类来解决问题

    def sumSubarrayMins(self, A):
        # 初始化结果和栈
        res, stack = 0, []
        
        # 在数组前后分别添加哨兵元素
        A = [float('-inf')] + A + [float('-inf')]

        for i, n in enumerate(A):
            # 当前值小于栈顶元素时，处理栈内元素
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            
            # 将当前索引入栈
            stack.append(i)
        
        # 返回结果对 10^9 + 7 取模后的值
        return res % (10 ** 9 + 7)

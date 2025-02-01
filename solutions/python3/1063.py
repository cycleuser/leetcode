
class Solution:
    # 定义一个解决方案类

    def validSubarrays(self, nums: List[int]) -> int:
        # 初始化栈和结果计数器
        stack, res = [], 0
        
        for num in nums:
            # 当前数字与栈顶元素比较，维护单调递增的栈
            while stack and stack[-1] > num:
                stack.pop()
            # 将当前数字压入栈中
            stack.append(num)
            # 累加当前栈长度到结果计数器
            res += len(stack)
        
        return res  # 返回最终的结果计数器值

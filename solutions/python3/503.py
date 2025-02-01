
class Solution:
    # 定义一个解决方案类

    def nextGreaterElements(self, nums):
        # 初始化栈和结果列表
        stack, res = [], [-1] * len(nums)
        
        for j in range(2):  # 遍历两次数组，以处理环形特性
            for i in range(len(nums)):
                # 当栈不为空且当前元素大于栈顶对应位置的元素时，更新结果列表并弹出栈顶
                while stack and (nums[stack[-1]] < nums[i]):
                    res[stack.pop()] = nums[i]
                
                # 如果是第二次遍历且栈为空，则停止
                if j == 1 and not stack: 
                    break
                
                # 将当前索引压入栈中
                stack += i,
        
        return res  # 返回结果列表

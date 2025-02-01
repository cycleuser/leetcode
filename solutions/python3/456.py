
class Solution:
    # 检查数组中是否存在132模式
    
    def find132pattern(self, nums):
        stack, s3 = [], -float("inf")
        
        for n in nums[::-1]:  # 遍历逆序的nums列表
            # 如果当前元素小于s3，则找到了132模式，返回True
            if n < s3:
                return True
            
            # 尝试更新s3并移除栈中比n小的元素
            while stack and stack[-1] < n:
                s3 = stack.pop()
            
            # 将当前元素压入栈中
            stack.append(n)
        
        # 遍历结束，未找到132模式，返回False
        return False

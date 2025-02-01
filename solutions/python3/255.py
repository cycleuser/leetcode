
class Solution:
    # 检查给定的前序遍历列表是否有效
    def verifyPreorder(self, preorder):
        # 使用栈辅助，lower表示上一个元素的值
        stack, lower = [], -float("inf")
        
        for x in preorder:
            # 如果当前值小于lower，则无效
            if x < lower: 
                return False
            
            # 当栈不为空且当前值大于栈顶元素时，更新lower并弹出栈顶元素
            while stack and x > stack[-1]: 
                lower = stack.pop()
            
            # 将当前值压入栈中
            stack.append(x)
        
        # 如果遍历完整个列表都没有返回False，则前序遍历有效
        return True

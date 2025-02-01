
class Solution:
    def largestRectangleArea(self, heights):
        """
        输入：heights -- List[int], 表示柱状图的高度列表
        输出：int，表示能够容纳的最大矩形面积

        1. 在高度列表末尾添加一个0，确保栈处理完所有元素。
        2. 使用一个单调递增的栈来追踪可能的矩形宽度。
        3. 遍历每一个柱子高度：
           - 如果当前柱子高度小于栈顶柱子的高度，则弹出栈顶元素并计算以该柱子为高的最大矩形面积；
           - 更新答案变量ans，存储最大的矩形面积。
        4. 将末尾添加的0移除，并返回最终的答案。
        """
        heights.append(0)  # Append a zero to handle the stack properly
        stack = [-1]       # Initialize stack with an artificial index -1
        ans = 0            # Initialize maximum area
        
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Pop and get the height of the popped element
                w = i - stack[-1] - 1      # Calculate width, -1 to exclude current index
                ans = max(ans, h * w)      # Update maximum area if needed
            
            stack.append(i)  # Push current index onto stack
        
        heights.pop()     # Remove the artificial zero added at the end
        
        return ans         # Return the maximum area found

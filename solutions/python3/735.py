
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # 使用栈来模拟碰撞过程
        # 中文：使用栈来模拟小行星碰撞的过程
        stack = []
        
        for asteroid in asteroids:
            # 将当前小行星加入栈中
            stack.append(asteroid)
            
            # 只要栈中有两个元素且满足左正右负的情况，就进行碰撞检查
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                # 中文：如果右侧小行星的绝对值大于左侧，则右侧存活
                if abs(stack[-1]) > stack[-2]:
                    stack.pop(-2)
                # 如果左侧小行星完全吸收右侧，移除左侧
                elif abs(stack[-1]) == stack[-2]:
                    stack.pop(-2)
                    stack.pop()
                # 否则左侧小行星被摧毁
                else:
                    stack.pop()
        
        return stack

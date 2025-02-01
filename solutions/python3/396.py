
class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        英文注释：定义一个类，包含一个方法用于计算数组A的最大旋转函数值。
        
        1. 初始化最大值mx和数组元素总和sm
        2. 遍历数组A的每个元素，累加当前下标*i*A[i]到mx中
            - 中文注释：初始化最大值mx及数组元素和sm。遍历计算初始的最大旋转函数值。
        
        3. 初始化当前值curr为mx，并从1开始遍历数组A
            - 中文注释：初始化当前的累积值curr，从第二个元素开始迭代更新
            - 英文注释：Initialize curr with the initial max value and start iterating from the second element.
        
        4. 在每次循环中计算新的curr，并与最大值mx比较更新
            - 英文注释：Update curr by subtracting total sum and adding A[i-1] * length of array, then compare with mx to update it if necessary.
            - 中文注释：在每一次迭代中根据公式更新当前的累积值，同时更新最大值。
        
        5. 返回最终的最大旋转函数值mx
            - 英文注释：Return the maximum rotation function value.
            - 中文注释：返回计算得到的最大旋转函数值。  
        """
        mx, sm = 0, sum(A)
        for i in range(len(A)):
            mx += i * A[i]
        curr = mx
        for i in range(1, len(A)):
            curr = curr - sm + A[i - 1] * len(A)
            mx = max(mx, curr)
        return mx

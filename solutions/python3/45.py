
class Solution:
    def jump(self, nums):
        """
        :param nums: List[int] - 需要跳跃的数组，每个元素表示从当前位置可以跳的最大步数
        :return: int - 实现从起点到终点所需的最少跳跃次数
        """
        
        last = cur = jump = i = 0
        # 中文：使用last记录当前能到达的最远距离；cur用于更新最远距离；jump记录跳跃次数；i用于遍历数组
        # English: Use `last` to record the farthest distance that can be reached; use `cur` to update the farthest distance;
        #          use `jump` to count the number of jumps; and use `i` to traverse the array.
        
        while cur < len(nums) - 1:
            # 中文：当当前最远距离小于数组长度减一，进入循环
            # English: If the current farthest distance is less than the length of the array minus one, enter the loop
            
            while i <= last:
                # 中文：内部循环用于遍历last范围内的所有点，并更新当前能到达的最远距离cur
                # English: The inner loop traverses all points within the range of `last` and updates the current farthest distance `cur`.
                
                if i + nums[i] > cur:
                    cur = i + nums[i]
                i += 1
            
            last = cur
            jump += 1
        
        return jump

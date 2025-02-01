
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        :type numbers: List[int]  # 输入的整数列表
        :type target: int          # 需要找到和为目标值的两个数之和
        :rtype: List[int]         # 返回索引，从1开始计数
        
        双指针法：一个指针从数组开头出发（left），另一个指针从数组末尾出发（right）
        根据两数之和与目标值的关系调整指针位置直至找到正确解
        """
        left = numbers[0]  # 初始化左指针指向第一个元素
        right = numbers[-1]  # 初始化右指针指向最后一个元素
        
        i, j = 0, 0  # 分别记录左右指针对应的索引位置，初始为0
        
        while True:
            current_sum = left + right  # 计算当前两数之和
            
            if current_sum > target:  # 当前和大于目标值
                j += 1  # 右指针左移
                right = numbers[-1 - j]  # 更新右指针对应的数值
            elif current_sum < target:  # 当前和小于目标值
                i += 1  # 左指针右移
                left = numbers[i]  # 更新左指针对应的数值
            else:  # 找到正确解
                return [i + 1, len(numbers) - j]  # 返回索引（从1开始计数）

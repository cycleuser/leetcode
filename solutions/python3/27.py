
class Solution:
    # 定义移除元素的方法，返回新数组的长度和修改后的数组内容
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # 初始化索引指针
        for num in nums:  # 遍历列表中的每个元素
            if num != val:  # 如果当前元素不等于指定值val
                nums[i] = num  # 将该元素放到新数组对应位置
                i += 1  # 索引指针右移一位
        return i  # 返回新数组的实际长度

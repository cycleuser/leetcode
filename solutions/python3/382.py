
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 初始化时将链表转换为列表形式存储在arr中
    def __init__(self, head: ListNode):
        self.arr = []
        current = head  # 使用current指针遍历链表
        while current:
            self.arr.append(current.val)
            current = current.next

    # 随机返回arr中的一个元素，使用random.choice方法实现
    def getRandom(self) -> int:
        return random.choice(self.arr)

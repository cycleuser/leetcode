
class Solution:
    # 定义一个方法，用于将两个链表表示的数字相加
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s1, s2, s3 = [], [], []  # 初始化三个列表来存储节点值
        p1, p2 = l1, l2         # 指针初始化，指向链表的头结点
        
        # 将l1链表中的数字压入s1列表中
        while p1:
            s1.append(p1.val)
            p1 = p1.next
            
        # 将l2链表中的数字压入s2列表中
        while p2: 
            s2.append(p2.val)  
            p2 = p2.next
        
        # 确保s1的长度不小于s2，以便后续处理进位时更加方便
        if len(s1) < len(s2):
            s1, s2 = s2, s1  # 列表和链表互换
            l1, l2 = l2, l1
        
        residual = 0    # 初始化进位值为0
        
        # 当s1还有元素时，依次弹出并相加
        while len(s1) > 0:
            temp = s1.pop() + residual
            if len(s2) > 0: 
                temp += s2.pop()
            s3.append(temp % 10)    # 将结果的个位数存入s3中
            residual = temp // 10   # 更新进位值
        
        head, p = ListNode(1), l1    # 创建一个头节点并指向l1链表的第一个节点作为起始点

        head.next = p               # 将新创建的头节点连接到原链表上
        while len(s3) > 0: 
            p.val = s3.pop()        # 更新当前指针所指向节点的值为s3中的值
            p = p.next              # 移动指针至下一个节点

        return head if residual == 1 else head.next   # 返回头结点，如果存在进位则返回下一个节点

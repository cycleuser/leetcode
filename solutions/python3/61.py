
class Solution:
    # 定义一个方法用于向右旋转链表，k是旋转次数
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 初始化数组和计数器，数组用于存储节点指针，计数器用于统计链表长度
        arr, count = [head], 0
        root = last = head
        
        # 遍历链表，更新last（最后一个节点）并计算链表的总长度
        while last and last.next and count < k:
            last, count = last.next, count + 1
            arr.append(last)
        
        # 如果k不等于count，则需要调整k值为实际有效的旋转次数
        if k != count: 
            k = k % (count + 1)  # 计算实际需要的旋转次数
            last = arr[k]  # 更新last为新的最后一个节点
        
        # 如果没有有效节点或无需旋转，直接返回原头结点
        if k == 0 or not last: 
            return head
        
        # 找到新的尾节点和原来的倒数第二个节点，并完成链表的重新连接
        curr = root
        while last.next:
            last, curr = last.next, curr.next
        last.next, curr.next, start = root, None, curr.next  # 新的头结点
        
        return start  # 返回旋转后的链表新头结点

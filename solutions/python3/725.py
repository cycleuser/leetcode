
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        """
        计算链表节点总数并确定每部分的长度和剩余节点数。
        
        :param root: 链表头节点
        :param k: 分割后的最大数量
        :return: 返回分割后的链表头节点列表
        """
        n = 0
        node = root
        # 计算链表总长度
        while node:
            n += 1
            node = node.next
        
        count = n // k  # 每部分的基本长度
        residual = n % k  # 剩余节点数，用于分配到前几部分

        i = 0
        ret = [[] for _ in range(k)]  # 初始化结果列表，大小为k的空列表
        prev = root
        while prev and k > 0:
            node = prev  # 当前部分的起始节点
            leftover = count  # 每个部分的基本长度计数器

            ret[i] = node  # 将当前部分的头节点添加到结果列表中
            i += 1

            while node and leftover > 1:  # 遍历当前部分，直到达到基本长度减一
                node = node.next
                leftover -= 1
            
            if node and count != 0 and residual:
                # 如果还有剩余节点且当前部分还未满，则继续分配一个节点
                node = node.next
                residual -= 1

            prev = node.next if node else None  # 更新prev指针，指向下一个部分的起始位置或None
            if node:  # 断开当前部分与后续链表的连接
                node.next = None
            
            k -= 1  # 减少剩余的部分数量
        
        return ret  # 返回分割后的链表头节点列表

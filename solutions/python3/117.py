
class Solution:
    def connect(self, root: "Node") -> "Node":
        # 使用虚拟节点简化链表操作，便于连接子节点
        dummy = Node(-1, None, None, None)
        
        tmp = dummy  # 暂存节点用于构建next指针
        res = root  # 原始根节点
        
        while root:
            # 遍历当前层的所有节点
            while root:
                if root.left:  # 如果当前节点有左子节点
                    tmp.next = root.left  # 将虚拟节点的下一个指向左子节点
                    tmp = tmp.next       # 更新tmp到新的节点上
                
                if root.right:  # 如果当前节点有右子节点
                    tmp.next = root.right  # 将虚拟节点的下一个指向右子节点
                    tmp = tmp.next         # 更新tmp到新的节点上
                
                root = root.next   # 移动到下一节点
            
            # 遍历下一层
            root = dummy.next  # 从下一层的第一个节点开始
            tmp = dummy        # 重置tmp为虚拟头结点
            dummy.next = None  # 清空虚拟节点的next指针，准备下一次循环

        return res  # 返回原始根节点

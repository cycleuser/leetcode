
class Solution:
    # 复制随机链表
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 使用字典存储新旧节点的映射关系，便于快速查找
        dic = collections.defaultdict(lambda: Node(0, None, None))
        dic[None] = None  # 处理空指针情况

        # 遍历原链表构建新的链表结构
        n = head
        while n:
            # 设置新节点的值、next和random属性
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        
        return dic[head]  # 返回复制后的链表头节点

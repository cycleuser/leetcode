
class Solution:
    def treeToDoublyList(self, root):
        # 初始化头节点和尾节点指针
        head, tail = [None], [None]

        # 深度优先搜索函数，参数为当前节点和前驱节点
        def dfs(node, pre):
            if not node:
                return

            # 递归处理左子树
            l = dfs(node.left, pre)

            # 创建新节点，并连接前驱节点
            new_node = Node(node.val, l or pre, None)
            if pre and not l:
                pre.right = new_node
            elif l:
                l.right = new_node

            # 更新头尾节点指针
            if not pre and not l:
                head[0] = new_node
            if not tail[0] or node.val > tail[0].val:
                tail[0] = new_node

            # 递归处理右子树
            r = dfs(node.right, new_node)
            return r if r else new_node
        
        # 开始深度优先搜索，从根节点开始
        dfs(root, None)

        # 连接头尾节点形成循环链表
        if head[0]:
            head[0].left = tail[0]
            tail[0].right = head[0]

        return head[0]

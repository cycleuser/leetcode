
class Solution:
    # 判断两棵树是否相同，采用递归方法比较两个树的每个节点
    def isSameTree(self, p, q):
        # 如果两个节点都为空，则它们相同
        if not p and not q:
            return True
        # 仅当p和q都不为空时才进一步比较其值以及子节点
        elif p and q:
            # 当前节点的值相等且左右子树均相同则两棵树相同
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # 其他情况，即一个为空而另一个不为空，或节点值不同，则树不相同
            return False

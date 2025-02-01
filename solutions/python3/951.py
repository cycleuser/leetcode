
class Solution:
    # 解决方案类

    def flipEquiv(self, root1, root2):
        # 如果其中一个节点为空，检查两个节点是否同时为空
        if not root1 or not root2: 
            return root1 == root2
        
        # 检查左右子节点的值是否相等或不一致的情况
        if (root1.left and root2.left and root1.left.val != root2.left.val) \
           or (not root1.left and root2.left) or (root1.left and not root2.left):
            # 如果不匹配，交换root1的左右子节点
            root1.left, root1.right = root1.right, root1.left
        
        # 递归检查当前节点及其子树是否翻转等价
        return root1.val == root2.val and self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)

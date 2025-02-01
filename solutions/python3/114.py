
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    层序遍历二叉树，将每个节点的左子树移到其右子树，并断开左子树链接。
    
    :type root: TreeNode
    :rtype: 无返回值，直接在原树上修改
    
    中文注释：
    - 定义一个辅助函数 traverse，用于递归遍历节点
    - 如果当前节点为空，则直接返回
    - 递归调用 traverse 函数处理左子树和右子树
    - 将当前节点的左子树移到右子树，并断开左子树链接
    - 返回调整后的最右侧节点
    """
    def flatten(self, root):
        # 中文注释：开始遍历操作，修改原树结构
        def traverse(node):
            if not node: return None  # 如果当前节点为空，则返回None
            left, right = traverse(node.left), traverse(node.right)  # 递归处理左右子树
            if node.left: 
                node.right, node.left = node.left, None  # 将左子树移到右子树，断开原左子树链接
            return right if right else left if left else node  # 返回调整后的最右侧节点

        traverse(root)  # 开始遍历根节点


class Solution:
    # 构建二叉树的递归函数，输入中序遍历和后序遍历的结果列表
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            # 找到当前根节点在中序遍历中的索引位置，并弹出后序遍历中的最后一个元素作为当前子树的根节点值
            ind = inorder.index(postorder.pop())
            
            # 递归构建右子树，左闭右开区间 [ind+1:] 表示从索引 ind+1 开始到末尾
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            
            # 递归构建左子树，左闭右闭区间 [:ind] 表示从起始到索引 ind-1 结束
            root.left = self.buildTree(inorder[:ind], postorder)
            
            return root

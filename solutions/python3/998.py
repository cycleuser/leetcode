
class Solution:
    # 定义插入最大值的函数，输入根节点root、要插入的值val以及父节点parent
    def insertIntoMaxTree(self, root: TreeNode, val: int, parent = None) -> TreeNode:
        # 如果当前节点为空或新值大于当前节点值，则创建新节点，并调整父子关系
        if not root or val > root.val:
            new = TreeNode(val)
            new.left = root  # 将原根节点作为新插入节点的左子树

            if parent:  # 如果存在父节点
                if parent.right == root:  # 若当前节点是父节点的右孩子，则将新节点设为父节点的新右孩子
                    parent.right = new
                else:  # 否则，设置为父节点的左子树
                    parent.left = new

            return new  # 返回新根节点
        else:
            # 如果当前节点值大于插入值，则递归地将新值插入到右子树中
            root.right = self.insertIntoMaxTree(root.right, val, root)
        
        return root  # 返回调整后的根节点

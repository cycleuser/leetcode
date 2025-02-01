
class Solution:
    def constructFromPrePost(self, pre, post):
        """
        构造二叉树，给定前序和后序遍历结果
        
        :param pre: List[int] - 前序遍历列表
        :param post: List[int] - 后序遍历列表
        :return: TreeNode - 构建的二叉树根节点
        """
        if pre:
            root = TreeNode(pre.pop(0))  # 弹出并设置前序遍历的第一个元素为根节点
            post.pop()  # 移除后序遍历中的最后一个元素，因为它已与根节点匹配
            
            if pre:  # 确保列表不为空
                if pre[0] == post[-1]:  # 检查左子树的前序首元素是否等于后序尾元素
                    root.left = self.constructFromPrePost(pre, post)  # 递归构建左子树
                else:
                    l_idx = post.index(pre[0])  # 找到左子树在后序遍历中的索引
                    r_idx = pre.index(post[-1])  # 找到右子树在前序遍历中的索引
                    
                    root.left = self.constructFromPrePost(pre[:r_idx], post[:l_idx + 1])  # 递归构建左子树
                    root.right = self.constructFromPrePost(pre[r_idx:], post[l_idx + 1:])  # 递归构建右子树
            
            return root

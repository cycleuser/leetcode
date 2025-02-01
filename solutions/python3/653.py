
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        
        问题描述：给定一个二叉搜索树和一个目标值 k，判断是否存在两个元素的和为 k。
        
        方法思路：
            - 使用深度优先遍历（DFS）来查找满足条件的两个数。
            - 在遍历过程中，维护一个字典 dic 来记录已经访问过的节点值及其补数。
            - 如果当前节点值在字典中找到，则说明存在两个元素和为 k。
        """
        def traverse(node):
            """
            深度优先遍历二叉搜索树。

            :param node: 当前遍历的节点
            :return: bool，表示是否找到满足条件的两个数
            """
            if not node: return False  # 如果当前节点为空，则返回False
            
            diff = k - node.val  # 计算目标值与当前节点值的差值
            if diff in dic:       # 检查该差值是否存在在字典中，若存在则说明找到满足条件的两个数
                return True
            else:
                dic[node.val] = 1  # 将当前节点值存入字典
            
            # 继续遍历左子树和右子树，只要有一个返回True即满足条件
            return traverse(node.left) or traverse(node.right)
        
        dic = {}  # 初始化字典用于存储已经访问过的节点值及其补数
        return traverse(root)  # 开始深度优先遍历从根节点开始

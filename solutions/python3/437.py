
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 寻找二叉树中和为sum的路径数量
    # :type root: TreeNode  根节点
    # :type sum: int        目标和
    # :rtype: int           路径数
    def pathSum(self, root, sum):
        dic = {}  # 存储以每个节点为结尾的路径和
        
        # 深度优先遍历，计算所有路径和并统计目标和出现次数
        def traverse(node, parent):
            if not node: return

            dic[node] = [node.val]  # 初始化当前节点路径和列表
            
            # 如果当前节点值等于目标和，则路径数+1
            if node.val == sum:
                res[0] += 1
            
            # 更新父节点的路径和到当前节点，并检查是否形成目标和
            if parent:
                for num in dic[parent]:
                    dic[node].append(num + node.val)
                    if num + node.val == sum:
                        res[0] += 1

            traverse(node.left, node)  # 遍历左子树
            traverse(node.right, node)  # 遍历右子树
        
        res = [0]
        traverse(root, None)  # 开始遍历
        return res[0]

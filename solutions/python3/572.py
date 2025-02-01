
class Solution:
    # 判断t是否为s的子树
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        
        通过遍历生成字符串的方式判断两棵树的内容是否匹配，进而确定t是否是s的子树。
        
        思路：对每个节点进行遍历，使用特殊字符标记节点值，并递归处理左右子树。在最终比较时，直接检查两个字符串是否包含关系。
        """
        
        def traverse(node):
            # 递归生成表示当前树结构的字符串
            if not node: 
                return "^"  # 空节点用"^"表示
            return "$"+str(node.val)+"?"+traverse(node.left)+"@"+traverse(node.right)  # 根据节点值及左右子树构造唯一标识
            
        s_str = traverse(s)  # 获取s的字符串表示
        t_str = traverse(t)  # 获取t的字符串表示
        
        return t_str in s_str  # 检查t是否为s的子串

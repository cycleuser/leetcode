
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        """
        构建所有可能的单叶二叉树，节点总数为N。
        
        Parameters:
            N (int): 树中结点数
        
        Returns:
            List[TreeNode]: 包含所有可能构建的单叶二叉树根节点的列表
        """

        def constr(N: int) -> Generator[TreeNode, None, None]:
            """
            生成满足条件的所有可能的单叶二叉树。
            
            Parameters:
                N (int): 当前子树需要填充的结点数
            
            Returns:
                Generator[TreeNode]: 包含所有可能构建的单叶二叉树根节点的生成器
            """
            if N == 1: 
                yield TreeNode(0)
            else:
                for i in range(1, N, 2):
                    # 遍历左子树结点数，右子树结点数由剩余决定
                    for l in constr(i):  
                        for r in constr(N - i - 1): 
                            m = TreeNode(0)  # 创建根节点
                            m.left = l       # 左子树连接到根节点
                            m.right = r      # 右子树连接到根节点
                            yield m          # 返回生成的单叶二叉树

        return list(constr(N))  # 将生成器转换为列表

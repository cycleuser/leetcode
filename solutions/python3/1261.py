
class FindElements:
    # 初始化方法，用于设置根节点和存储结果的集合
    def __init__(self, root: TreeNode):
        self.root = root  # 根节点初始化
        self.nums = set()  # 存储处理后的值的集合
        self.dfs(root)  # 调用dfs方法进行后续处理

    # 深度优先搜索方法，用于递归地为树中的每个节点赋值并存储其值
    def dfs(self, node: TreeNode, real: int = 0):
        if node:
            node.val = real  # 设置当前节点的值
            self.nums.add(node.val)  # 将该节点的值加入集合中
            self.dfs(node.left, real * 2 + 1)  # 递归处理左子节点
            self.dfs(node.right, real * 2 + 2)  # 递归处理右子节点

    # 查找方法，检查给定的目标值是否存在于结果集合中
    def find(self, target: int) -> bool:
        return target in self.nums  # 返回目标值是否存在在集合中

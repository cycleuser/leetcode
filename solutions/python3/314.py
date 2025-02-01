
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 该方法用于按垂直顺序遍历二叉树并返回节点值列表
    def verticalOrder(self, root: 'TreeNode') -> list[list[int]]:
        # 初始化队列和字典，记录每个垂直线上的节点值
        q, arrays = (root and collections.deque([(root, 0)]) or None), collections.defaultdict(list)
        
        while q:
            # 创建一个新的deque来存储下一层的节点及其索引
            new = collections.deque()
            
            for node, ind in q:
                # 将当前节点值添加到对应的垂直线列表中
                arrays[ind].append(node.val)
                
                if node.left:  # 如果左子节点存在，将其加入队列并调整索引为-1
                    new.append((node.left, ind - 1))
                    
                if node.right:  # 如果右子节点存在，将其加入队列并调整索引为+1
                    new.append((node.right, ind + 1))
            
            q = new  # 更新当前层的队列为下一层的队列

        # 按照垂直线索引排序并返回结果
        return [arr for i, arr in sorted(arrays.items())]

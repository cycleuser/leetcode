
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        判断给定的前序序列是否可以构成一棵有效的二叉树

        :param preorder: 字符串形式的前序遍历序列，节点间用逗号分隔
        :return: 如果该前序序列能构成有效二叉树，则返回 True；否则返回 False
        """
        stack = []
        
        for c in preorder.split(','):
            # 将当前字符压入栈中
            stack.append(c)
            
            # 当栈顶两个元素为 '#' 时，进行处理
            while len(stack) > 1 and stack[-2:] == ['#', '#']:
                # 弹出栈顶的两个 '#' 
                stack.pop()
                stack.pop()
                
                # 如果此时栈为空，则当前序列无法构成有效二叉树
                if not stack:
                    return False
                
                # 弹出下一个元素，并压入一个 '#' 表示已处理该节点的子树
                stack.pop()
                stack.append('#')
        
        # 最终检查栈是否只包含一个 '#'，则说明可构成有效二叉树
        return stack == ['#']

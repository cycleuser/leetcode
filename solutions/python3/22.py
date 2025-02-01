
class Solution:
    # Python 解决括号生成问题

    def generateParenthesis(self, n: int) -> List[str]:
        # 使用广度优先搜索（BFS）来构建所有可能的括号组合
        bfs = [(0, 0, '')]  # 初始化状态队列，每个元素为 (左括号数, 右括号数, 当前生成的字符串)
        
        for c in range(n * 2):  # 遍历生成 n 对括号的所有可能组合
            bfs = [(l + 1, r, s + '(') for l, r, s in bfs if l + 1 <= n] + \
                  [(l, r + 1, s + ')') for l, r, s in bfs if l - r]
        
        # 返回最终生成的所有有效括号字符串
        return [s for l, r, s in bfs]

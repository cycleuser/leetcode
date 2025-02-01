
class Solution:
    # 定义一个生成可能的下一步移动的方法
    def generatePossibleNextMoves(self, s: str) -> list[str]:
        # 使用列表推导式找到所有相邻且相等为'+'的索引对，并将这些位置替换为"--"
        return [s[:i] + "--" + s[i + 2:] for i in range(len(s) - 1) if s[i] == s[i + 1] == "+"]


class Solution:
    # 检查给定的数独是否有效

    def isValidSudoku(self, board):
        rows, cols, triples = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)

        # 遍历每一行和每一列，检查每个数字是否出现重复
        for i, row in enumerate(board):  # 遍历board中的每一行
            for j, c in enumerate(row):  # 遍历当前行中的每一个元素
                if c != ".":  # 如果不是空格"."
                    # 检查该数字是否已经在当前行、列或子方块中出现过
                    if c in rows[i] or c in cols[j] or c in triples[(i // 3, j // 3)]:
                        return False

                    # 将该数字添加到对应的集合中
                    rows[i].add(c)
                    cols[j].add(c)
                    triples[(i // 3, j // 3)].add(c)

        # 如果所有检查都通过，返回True表示数独有效
        return True

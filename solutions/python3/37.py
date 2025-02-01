
class Solution:
    def solveSudoku(self, board):
        # 初始化行、列和宫集合，用于存储已填数字；使用双端队列记录待填充位置
        rows, cols, triples, visit = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.deque([])
        
        for r in range(9):
            for c in range(9):
                # 遍历棋盘，填充已有的数字到相应集合中，并记录待填充位置
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])
                else:
                    visit.append((r, c))
        
        def dfs():
            # 当没有待填充位置时，表示已经成功填满整个棋盘
            if not visit:
                return True
            
            r, c = visit[0]
            t = (r // 3, c // 3)
            
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                # 检查当前数字是否可以填入
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig  # 填充数字并记录状态
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    
                    visit.popleft()  # 移除当前待填充位置
                    
                    if dfs():
                        return True  # 如果递归填满成功，直接返回

                    board[r][c] = "."  # 回溯
                    rows[r].discard(dig)  # 取消状态修改
                    cols[c].discard(dig)
                    triples[t].discard(dig)
                    
                    visit.appendleft((r, c))  # 将当前位置重新加入待填充队列

            return False
        
        dfs()

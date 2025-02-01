
class Solution:
    # 定义移动规则字典，用于记录每个位置可以移动到的位置
    def slidingPuzzle(self, board):
        moves, used, cnt = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}, set(), 0
        # 将初始状态转换为字符串形式便于比较和存储
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]  # 初始化队列，包含当前状态及其0的位置索引

        while q:
            new = []
            for s, i in q:
                used.add(s)  # 记录已访问的状态
                if s == "123450":
                    return cnt  # 如果达到目标状态，返回移动次数
                arr = [c for c in s]  # 将当前字符串状态转换为列表形式便于修改
                for move in moves[i]:  # 遍历当前索引可以到达的位置
                    new_arr = arr[:]  # 复制原数组
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]  # 进行交换操作
                    new_s = "".join(new_arr)  # 将新列表转换回字符串形式
                    if new_s not in used:  # 如果未访问过该状态，则加入队列
                        new.append((new_s, move))
            cnt += 1  # 移动次数加一
            q = new  # 更新队列为新的可能状态

        return -1  # 如果无法达到目标状态，返回-1

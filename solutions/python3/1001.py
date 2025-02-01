
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 初始化灯的状态集合和方向计数器
        lampsOn = set()
        rowsOn = collections.defaultdict(int)
        colsOn = collections.defaultdict(int)
        diagOnTopLeftBottomRight = collections.defaultdict(int)
        diagOnBottomLeftTopRight = collections.defaultdict(int)

        # 将所有开启的灯的位置添加到集合中，并更新方向计数器
        for r, c in lamps:
            lampsOn.add((r, c))
            rowsOn[r] += 1
            colsOn[c] += 1
            diagOnTopLeftBottomRight[c - r] += 1
            diagOnBottomLeftTopRight[c + r - N] += 1

        # 存储查询结果的列表
        result = []

        # 对每个查询位置进行检查
        for r, c in queries:
            if rowsOn[r] > 0 or colsOn[c] > 0 or diagOnTopLeftBottomRight[c - r] > 0 or diagOnBottomLeftTopRight[c + r - N] > 0:
                result.append(1)  # 灯照亮
            else:
                result.append(0)  # 灯未照亮

            # 检查周围的灯并更新状态
            adjacentLamps = [(r, c), (r, c-1), (r, c+1), (r-1, c), (r-1, c-1), (r-1, c+1), (r+1, c), (r+1, c-1), (r+1, c+1)]
            for r, c in adjacentLamps:
                if (r, c) in lampsOn:
                    lampsOn.discard((r, c))
                    rowsOn[r] -= 1
                    colsOn[c] -= 1
                    diagOnTopLeftBottomRight[c - r] -= 1
                    diagOnBottomLeftTopRight[c + r - N] -= 1

        return result

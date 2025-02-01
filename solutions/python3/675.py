
class Solution:
    # 定义广度优先搜索函数来计算从起点到终点的最短路径（考虑障碍）
    def hadlocks(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])  # 获取森林的行数和列数
        processed = set()  # 已访问集合
        deque = collections.deque([(0, sr, sc)])  # 初始化队列，包含起始位置及其步数

        while deque:
            detours, r, c = deque.popleft()  # 弹出最近的节点和步数
            if (r, c) not in processed:  # 如果当前节点未被访问过
                processed.add((r, c))  # 标记为已访问

                # 检查是否到达目标位置，如果是，则返回已走过的步数及剩余路径长度
                if r == tr and c == tc:
                    return abs(sr - tr) + abs(sc - tc) + 2 * detours

                # 遍历四个方向的邻接节点
                for nr, nc, closer in ((r-1, c, r > tr), (r+1, c, r < tr),
                                       (r, c-1, c > tc), (r, c+1, c < tc)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:  # 检查边界和是否为障碍
                        if closer:  # 如果是更接近目标的节点
                            deque.appendleft((detours, nr, nc))
                        else:
                            deque.append((detours + 1, nr, nc))  # 否则，增加步数并加入队列

        return -1  # 搜索未成功找到路径时返回-1

    # 主函数用于计算砍伐所有树所需的最短时间
    def cutOffTree(self, forest):
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)  # 将所有树木的位置按高度排序

        sr = sc = ans = 0  # 起点位置
        for _, tr, tc in trees:  # 遍历每棵树的位置
            d = self.hadlocks(forest, sr, sc, tr, tc)  # 计算从当前起点到该树的最短路径
            if d < 0: return -1  # 如果无法到达，则返回-1

            ans += d  # 累加路径长度
            sr, sc = tr, tc  # 更新起始位置为上一棵树的位置

        return ans  # 返回总耗时

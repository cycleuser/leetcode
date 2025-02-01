
class Solution:
    """
    定义一个解决方案类，包含minRefuelStops方法用于计算加油次数。
    """

    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        # 使用优先队列存储状态 (加满油的操作数, 当前油量的负值, 当前位置, 操作索引)
        q = [(0, -startFuel, 0, 0)]
        n = len(stations)
        memo = set()

        while q:
            # 弹出优先队列顶部的状态
            refill, fuel, pos, index = heapq.heappop(q)
            fuel *= -1

            # 如果已遍历所有加油站且有足够的油量到达目标，则返回操作数
            if index == n and fuel - (target - pos) >= 0:
                return refill
            
            else:
                # 当前位置和加油量
                sPos, add = stations[index]

                # 检查当前状态是否已经处理过，以及是否有足够的油量通过下一个站点
                if (index, refill) not in memo and fuel - (sPos - pos) >= 0:
                    memo.add((index, refill))
                    # 根据选择加油或不加油的情况入队
                    heapq.heappush(q, (refill + 1, (fuel - (sPos - pos) + add) * -1, sPos, index + 1))
                    heapq.heappush(q, (refill, (fuel - (sPos - pos)) * -1, sPos, index + 1))

        # 如果没有可行解，返回-1
        return -1

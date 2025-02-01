
class Solution:
    # 定义一个解决方案类，用于解决给定的两城市计划成本问题

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        计算使两个城市的人参加计划所需的最小总成本。

        参数:
        - costs (List[List[int]]): 每个人参加两个城市的成本，格式为 [去A城的成本, 去B城的成本] 的列表

        返回值:
        - int: 使得两组人数相等且成本最低的总成本
        """
        
        # 根据去两个城市成本差排序，优化选择顺序
        costs.sort(key=lambda x: abs(x[0] - x[1]))

        a = b = 0  # 初始化前往A城和B城的人数为0
        N = len(costs) // 2  # 计算总人数的一半作为每组的目标人数

        c = 0  # 总成本初始化为0
        
        for c1, c2 in costs[::-1]:  # 反向遍历排序后的列表以优先选择差异较小的成本组合
            if c1 <= c2 and a < N or b >= N:  # 若当前人去A城更划算且A城人数未满，或B城人数已满，则去A城
                c += c1
                a += 1
            else:
                c += c2
                b += 1

        return c  # 返回最小总成本

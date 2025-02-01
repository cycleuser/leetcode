
class Solution:
    def getSkyline(self, buildings):
        # 创建事件列表，包含建筑物的左边界和右边界事件，并排序
        # 事件表示为 (位置, 高度, 结束位置)，使用负高度表示开始事件，0 表示结束事件
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        
        # 初始化结果列表和优先队列
        res, hp = [[0, 0]], [(0, float("inf"))]
        
        # 遍历所有事件
        for x, negH, R in events:
            # 调整高度堆，移除不再有效的建筑物高度
            while x >= hp[0][1]:
                heapq.heappop(hp)
            
            # 如果当前事件为建筑物开始，则将其高度加入优先队列
            if negH: 
                heapq.heappush(hp, (negH, R))
            
            # 判断并更新最高高度变化情况
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        
        # 返回结果列表（去掉第一个默认的[0, 0]）
        return res[1:]

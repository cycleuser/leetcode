
class Solution:
    # 定义一个解决方案类
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        # 使用defaultdict来记录每个标签的使用次数
        cnt = collections.defaultdict(int)
        
        # 构建一个包含负值和标签的堆，以便可以找到最大的values
        heap = [[-a, b] for a, b in zip(values, labels)]
        heapq.heapify(heap)  # 将列表转换为堆
        
        use = sm = 0  # 初始化使用次数和总和
        
        # 当剩余想要的数量大于零且堆中还有元素时
        while use < num_wanted and heap:
            a, b = heapq.heappop(heap)  # 弹出堆顶元素（当前最大的值及其对应的标签）
            
            if cnt[b] < use_limit:  # 检查该标签是否已达到限制
                sm -= a  # 更新总和，减去当前弹出的负值（相当于加上正值）
                use += 1  # 增加使用次数
                cnt[b] += 1  # 标记此标签已被使用一次
        
        return sm  # 返回最终的总和

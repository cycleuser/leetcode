
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 定义拓扑排序函数
        def topo_sort(points, pre, suc):
            order = []
            sources = [p for p in points if not pre[p]]
            while sources:
                s = sources.pop()
                order.append(s)
                for u in suc[s]:
                    pre[u].remove(s)
                    if not pre[u]:
                        sources.append(u)
            return order if len(order) == len(points) else []
        
        # 找到每个物品所属的组
        group2item = collections.defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group2item[group[i]].add(i)

        # 找到组与组之间以及同一组内物品之间的关系
        t_pre, t_suc = collections.defaultdict(set), collections.defaultdict(set)
        g_pre, g_suc = collections.defaultdict(set), collections.defaultdict(set)
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    t_pre[i].add(j)
                    t_suc[j].add(i)
                else:
                    g_pre[group[i]].add(group[j])
                    g_suc[group[j]].add(group[i])

        # 对组进行拓扑排序
        groups_order = topo_sort([i for i in group2item], g_pre, g_suc)

        # 对每个组内的物品进行拓扑排序
        t_order = []
        for i in groups_order:
            items = group2item[i]
            i_order = topo_sort(items, t_pre, t_suc)
            if len(i_order) != len(items):
                return []
            t_order += i_order

        return t_order if len(t_order) == n else []


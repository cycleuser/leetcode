
class Solution:
    # 初始化图和相关数据结构
    def sequenceReconstruction(self, org, seqs):
        from collections import defaultdict, set

        order, orders, graph, seen = defaultdict(int), set(), defaultdict(set), set()

        # 构建图和seen集合
        for seq in seqs:
            for i in range(len(seq)):
                if i > 0:
                    if seq[i] == seq[i - 1]: return False  # 检查序列中是否有重复元素
                    graph[seq[i - 1]].add(seq[i])  # 构建图，记录前一个节点到后一个节点的关系

            seen.add(seq[i])

        if not seen: 
            return False  # 如果seen为空，返回False

        # 根据org逆序遍历并计算order
        for i in range(len(org) - 1, -1, -1):
            if org[i] in seen:
                seen.discard(org[i])

            order[org[i]] = max([order[v] for v in graph[org[i]]] or [0]) + 1

            before = set(v for v in graph[org[i]] if v in seen)
            # 检查当前节点的order是否合理以及before集合是否为空
            if order[org[i]] in orders or before:
                return False
        
        # 如果seen为空，表示重建成功
        return not seen

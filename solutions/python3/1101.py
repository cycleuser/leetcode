
class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        """
        最早连接所有节点的时间。
        
        :param logs: 包含 [时间戳, 人A, 人B] 的日志列表
        :type logs: List[List[int]]
        :param N: 节点总数
        :type N: int
        :return: 连接所有节点的最早时间，如果无法连接则返回 -1
        :rtype: int
        """
        
        def root(a):
            """查找根节点并路径压缩"""
            return a if parent[a] == a else root(parent[a])
        
        # 初始化并查集
        parent = [i for i in range(N)]
        
        time = -1
        # 按时间戳排序日志，从最早的开始处理
        for t, a, b in sorted(logs):
            A, B = root(a), root(b)
            
            # 合并两个集合
            parent[A] = parent[a] = parent[b] = B
            
            if A != B:
                time = t  # 只有当两个不同的节点合并时更新时间
        
        # 检查是否所有节点都在同一个集合中
        return time if all(root(a) == root(b) for a, b in zip(parent, parent[1:])) else -1

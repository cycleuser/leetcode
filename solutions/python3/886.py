
class Solution:
    # 定义合并函数，尝试将节点node划分为组p
    def merge(self, node: int, p: int, group: list[int], disliked: dict[int, set[int]]) -> bool:
        # 将节点node划分到组p中
        group[node] = p
        
        # 遍历disliked中的连接节点v
        for v in disliked[node]:
            # 如果节点v已经属于相同的分组或者未被正确划分，返回False
            if group[v] == p or (group[v] == v and not self.merge(v, -p, group, disliked)):
                return False
        
        # 成功划分所有连接节点到不同组别
        return True

    # 定义判断是否可以二分图划分的函数
    def possibleBipartition(self, N: int, dislikes: list[list[int]]) -> bool:
        # 初始化分组列表和不喜欢关系字典
        group = [i for i in range(N + 1)]
        disliked = collections.defaultdict(set)
        
        # 建立不喜欢关系图
        for a, b in dislikes:
            disliked[a].add(b)
            disliked[b].add(a) 

        # 尝试将每个节点划分到不同组别
        for i in range(1, N + 1):
            if group[i] == i and not self.merge(i, 2001, group, disliked): 
                return False
        
        # 如果所有节点都能正确划分，返回True
        return True


class Solution:
    def accountsMerge(self, accounts):
        # 使用字典存储每个邮件地址的邻接关系，并记录所有邮箱的所有者
        def explore(mail, q):
            q += mail,
            visited.add(mail)
            for v in edges[mail]:
                if v not in visited: 
                    explore(v, q)  # 深度优先搜索，将未访问过的邻居加入队列
            return q
        
        # 初始化邻接关系表、邮箱所有者字典以及已访问集合和结果列表
        edges, owner, visited, res = collections.defaultdict(list), {}, set(), []
        
        for acc in accounts:
            # 记录每个账户的首个元素作为所有者信息，其余元素表示联系人邮件地址
            owner[acc[1]] = acc[0]
            for i in range(1, len(acc) - 1):
                if acc[i] != acc[i + 1]:
                    edges[acc[i]] += acc[i + 1],  # 添加邻接关系，确保对称性
                    edges[acc[i + 1]] += acc[i],
        
        for acc in accounts:
            # 如果当前账户的所有者还未被访问过，则执行深度优先搜索
            if acc[1] not in visited: 
                res += [acc[0]] + sorted(explore(acc[1], [])),  # 将所有者的名称和按顺序的邮件地址添加到结果列表
        
        return res

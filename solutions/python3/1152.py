
class Solution:
    # 定义Solution类

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        import collections
        from itertools import combinations
        
        # 使用defaultdict存储每个用户的浏览网站列表
        dp = collections.defaultdict(list)
        
        # 使用Counter统计访问模式的出现次数
        count = collections.Counter()
        
        # 将timestamp, username, website按时间排序后遍历填充dp和count
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        
        # 统计每个用户的3个网站组合出现的频率
        for u in dp:
            count += collections.Counter(set(combinations(dp[u], 3)))
        
        # 找到访问模式中最大的访问次数
        target = max(count.values())
        
        # 返回访问次数最多的3个网站组合，取字典键值最小的一个
        return min(list(k) for k in count if count[k] == target)

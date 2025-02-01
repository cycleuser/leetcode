
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # 初始化结果为0，使用列表形式便于后续更新最大值
        res = [0]
        
        # 使用集合存储已经计算过的情况以避免重复计算
        memo = set()
        
        def dfs(st: dict[int, int], zeros: int, ones: int, cnt: int) -> None:
            """
            深度优先搜索，尝试从当前字符串集合中选择最优组合
            
            :param st: 当前剩余的可用字符串计数
            :param zeros: 剩余可用0的数量
            :param ones: 剩余可用1的数量
            :param cnt: 当前已选字符串数量
            """
            if (zeros, ones, cnt) not in memo:
                # 更新最大选择数量
                if cnt > res[0]:
                    res[0] = cnt
                
                if zeros or ones:
                    for s in st:
                        if st[s] and cntr[s]["0"] <= zeros and cntr[s]["1"] <= ones:
                            # 选择当前字符串并递归处理剩余情况
                            st[s] -= 1
                            dfs(st, zeros - cntr[s]["0"], ones - cntr[s]["1"], cnt + 1)
                            st[s] += 1
                
                memo.add((zeros, ones, cnt))
        
        # 计算每个字符串中0和1的个数
        cntr = {s: collections.Counter(s) for s in strs}
        
        # 调用深度优先搜索函数开始计算最大组合数量
        dfs(collections.Counter(strs), m, n, 0)
        
        return res[0]


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # 定义移除一个零闭集的函数
        def remove_one_zero_clique(non_zero):
            n = len(non_zero)
            q = collections.deque()            
            # 使用队列存储(index集合, 集合和值) 的元组
            q.append(([0], non_zero[0]))
            min_zero_set = None

            while q:
                cur_set, cur_sum = q.popleft()
                if cur_sum == 0:
                    min_zero_set = cur_set
                    break
                for j in range(cur_set[-1] + 1, n):
                    q.append((cur_set + [j], cur_sum + non_zero[j]))
            
            # 将找到的零闭集转换为集合
            min_zero_set = set(min_zero_set)
            return [non_zero[i] for i in range(n) if i not in min_zero_set]
        
        bal = collections.defaultdict(int)
        # 统计每个用户的余额变化情况，正数表示净收入，负数表示净支出
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        non_zero = [bal[k] for k in bal if bal[k] != 0]
        
        # 初始非零余额的数量
        bal_cnt = len(non_zero)
        while len(non_zero) > 0:
            # 移除一个零闭集，减少非零余额数量
            non_zero = remove_one_zero_clique(non_zero)
            bal_cnt -= 1
        return bal_cnt


from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # 使用字典存储每个名字的交易记录，键为名字，值为按时间排序的列表
        last = defaultdict(list)
        ret = set()  # 存储不合法的交易记录
        
        # 按时间排序处理每笔交易
        for name, time, amount, city in sorted([t.split(',') for t in transactions], key=lambda x: int(x[1])):
            if int(amount) > 1000:
                ret.add(','.join([name, time, amount, city]))  # 如果金额大于1000，标记交易为不合法
            
            # 检查最近一笔交易是否超过60分钟
            if name in last:
                for t, a, c in last[name][::-1]:
                    if int(time) - int(t) > 60: 
                        break  # 如果时间差超过60分钟，停止检查
                    if city != c:  # 如果城市不同，标记交易为不合法
                        ret.add(','.join([name, t, a, c]))
                        ret.add(','.join([name, time, amount, city]))
            
            # 将当前交易记录加入到字典中
            last[name].append([time, amount, city])
        
        return list(ret)

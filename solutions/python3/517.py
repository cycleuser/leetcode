
class Solution:
    # 定义一个用于查找移动次数最小值的方法
    def findMinMoves(self, machines):
        # 计算目标均值和机器总数，初始化累加和、结果变量以及总和
        target, n, sm, res, total = sum(machines) // len(machines), len(machines), 0, 0, sum(machines)
        
        # 检查总和是否满足均值整除条件
        if target * n != total:
            return -1
        
        # 遍历每台机器
        for i in range(n):
            # 计算左侧移水量、累加当前机器的容量、计算右侧移水量
            l, sm, r = target * i - sm, sm + machines[i], target * (n - i - 1) - total + sm + machines[i]
            
            # 更新最小移动次数结果
            res = max(res, l + r, l, r)
        
        return res


class Solution:
    # 定义一个用于获取因子列表的方法，输入为整数n
    def getFactors(self, n: int) -> List[List[int]]:
        factors = set()  # 保存所有小于sqrt(n)的因子
        # 遍历从2到根号n之间的所有整数i，寻找能整除n的因子
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors |= {i, n // i}  # 将因子及其对应的商加入集合
        
        q, res = [[f, [f]] for f in factors], []  # 初始化队列q和结果列表res
        while q:  # 当队列不为空时循环执行以下操作
            new = []  # 用于保存新生成的子集
            for sm, arr in q:  # 遍历当前队列中的每个元素(sm, arr)
                for f in factors:
                    if f >= arr[-1]:  # 确保新因子f不小于当前子集的最后一个数
                        if sm * f < n:
                            new.append([sm * f, arr + [f]])  # 增加新的子集到队列中
                        elif sm * f == n:  # 如果新因子使当前子集乘积等于n
                            res.append(arr + [f])  # 将其加入结果列表res
        
        return res  # 返回所有满足条件的因子组合列表

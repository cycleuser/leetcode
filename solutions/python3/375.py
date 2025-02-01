
class Solution:
    # 定义一个解题类，用于解决获取金额问题

    def getMoneyAmount(self, n):
        # 初始化一个字典来存储子问题的解以避免重复计算
        dic = {}

        # 定义一个深度优先搜索函数，用于查找最小花费
        def dfs(l, r):
            # 如果左索引大于等于右索引，则无需支付任何费用
            if l >= r: 
                return 0

            # 如果当前子问题尚未计算过结果，则进行计算并存储在字典中
            if (l, r) not in dic:
                dic[(l, r)] = min(num + max(dfs(l, num - 1), dfs(num + 1, r)) for num in range(l, r))

            # 返回已经计算好的结果
            return dic[(l, r)]

        # 调用dfs函数从1到n进行搜索，返回最小花费
        return dfs(1, n)

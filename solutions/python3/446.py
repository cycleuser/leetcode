
class Solution:
    def numberOfArithmeticSlices(self, A):
        # 使用字典嵌套结构存储差值及对应的子序列数量
        # defaultdict(dict) 是为了方便处理不存在的键值对，默认初始化为0或1
        dp = collections.defaultdict(dict)
        res = 0
        
        # 遍历数组A中的每一个元素
        for j in range(len(A)):
            # 再次遍历j之前的所有元素
            for i in range(j):
                diff = A[j] - A[i]
                
                # 更新差值对应的子序列数量
                dp[j][diff] = dp[j].get(diff, 0) + dp[i].get(diff, 1)
                
                # 检查是否存在满足条件的子数组，更新结果和dp表
                if diff in dp[i]:
                    res += dp[i][diff]
                    dp[j][diff] += 1
                    
        return res

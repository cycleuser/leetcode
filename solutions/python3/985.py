
class Solution:
    # 定义一个解决方案类

    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        # 初始化偶数和为0
        even_sum = sum(a for a in A if a % 2 == 0)
        
        # 遍历查询列表
        for i in range(len(queries)):
            val, ind = queries[i]
            
            # 更新偶数和：先减去旧值，再加新值
            even_sum -= A[ind] % 2 == 0 and A[ind]
            A[ind] += val
            
            # 更新偶数和：如果新值是偶数，则加上该值
            if A[ind] % 2 == 0:
                even_sum += A[ind]
            
            # 将当前计算出的偶数和赋给查询结果
            queries[i] = even_sum
        
        return queries
    # 返回处理后的查询结果列表

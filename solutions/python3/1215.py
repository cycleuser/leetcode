
class Solution:
    # 定义一个解决方案类
    
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        # 计算在一个给定范围内的步进数
        
        def dfs(n):
            # 深度优先搜索，生成满足条件的步进数
            if n > high:
                return  # 超出上限，停止递归
            
            if n >= low:
                q.add(n)  # 如果当前数字在有效范围内，则加入结果集

            d = n % 10
            if d == 0:
                dfs(n * 10 + 1)
            elif d == 9:
                dfs(n * 10 + 8)
            else:
                dfs(n * 10 + d + 1)
                dfs(n * 10 + d - 1)
        # 使用集合来存储满足条件的步进数
        q = set()
        
        for i in range(10):
            dfs(i)  # 从0到9开始递归生成符合条件的数字
        
        return sorted(q)  # 返回结果，按升序排列

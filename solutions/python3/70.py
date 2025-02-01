
class Solution:
    # 定义一个求解爬楼梯问题的类

    def climbStairs(self, n: int) -> int:
        # 定义一个爬楼梯方法，输入n表示台阶数，返回到达第n个台阶的方法总数
        
        memo = {}
        # 使用字典memo来存储已经计算过的子问题结果以避免重复计算

        def dfs(i):
            # 定义深度优先搜索辅助函数dfs
            if i >= n: 
                return 1 if i == n else 0
            # 当i大于等于n时，返回1表示当前路径有效；否则返回0
        
            if i not in memo:
                # 如果memo中没有保存过i的值，则递归计算并存储结果
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        # 返回从起点开始爬楼梯的方法总数

        return dfs(0)
        # 调用dfs(0)，表示从第0个台阶开始爬楼梯

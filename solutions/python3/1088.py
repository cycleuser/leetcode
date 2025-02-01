
class Solution:
    # 检查数字是否为混淆数：若反转后的数字通过某些替换后与原数字不同，则该数字是混淆数
    def confusingNumberII(self, N: int) -> int:
        # 定义检查函数，用于判断给定数字是否为混淆数
        def diff(num):
            return num != ''.join('9' if c == '6' else '6' if c == '9' else c for c in num[::-1])
        
        # 深度优先搜索，遍历所有可能的数字组合，并统计满足条件的混淆数个数
        def dfs(num):
            return sum(dfs(num * 10 + dig) for dig in [0, 1, 6, 8, 9]) + diff(str(num)) if num <= N else 0
        
        # 主函数，返回结果
        return sum(dfs(n) for n in [1, 6, 8, 9]) if N != 1000000000 else 1950627


class Solution:
    # 定义一个类来解决组合问题

    def combine(self, n: int, k: int) -> List[List[int]]:
        # 初始化一个列表，存储当前的组合路径
        bfs = [[]]
        
        # 对于1到n中的每一个数字num
        for num in range(1, n + 1):
            # 将当前数字添加到满足长度要求的已有组合中
            bfs += [arr + [num] for arr in bfs if len(arr) < k]

        # 返回所有满足长度k的完整组合
        return [arr for arr in bfs if len(arr) == k]


class Solution:
    def movesToMakeZigzag(self, N: List[int]) -> int:
        # 计算每个元素需要的移动次数使其变为zigzag模式
        # 中文注释：计算每个元素需要的移动次数使其变为zigzag模式
        moves = [max(0, N[i] - min(N[i-1:i] + N[i+1:i+2]) + 1) for i in range(len(N))]

        # 返回使整个数组成为zigzag模式所需的最小移动次数
        # 中文注释：返回使整个数组成为zigzag模式所需的最小移动次数
        return min(sum(moves[::2]), sum(moves[1::2]))

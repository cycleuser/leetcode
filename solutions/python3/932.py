
class Solution:
    # 定义一个类用于解决美丽数组问题

    def beautifulArray(self, N: int) -> List[int]:
        # 如果N为1，直接返回[1]
        if N == 1: 
            return [1]

        half = self.beautifulArray(N - N // 2)
        # 递归生成前半部分美丽数组
        even_half = [i * 2 for i in half if i * 2 <= N]
        # 生成偶数序列，确保所有元素不超过N
        odd_half = [i * 2 - 1 for i in half]
        # 生成奇数序列

        return even_half + odd_half
        # 将生成的偶数和奇数组合返回

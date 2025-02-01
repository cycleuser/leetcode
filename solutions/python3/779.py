
class Solution:
    # 定义一个求第N行第K列格子值的方法
    def kthGrammar(self, N: int, K: int) -> int:
        # 如果N大于1，递归计算前一层的值，并根据K的位置进行异或运算
        return N > 1 and self.kthGrammar(N - 1, (K + 1) // 2) ^ ((K - 1) % 2) or 0

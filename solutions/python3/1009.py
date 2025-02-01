
class Solution:
    # 求解位运算补数的方法，N为需要求补的数字，M可选参数初始为0，m用于辅助计算
    def bitwiseComplement(self, N: int, M = 0, m = 0) -> int:
        # 如果M大于等于N且M非零，则返回N和M的异或结果（位运算补数）
        return N ^ M if M and M >= N else self.bitwiseComplement(N, M + 2 ** m, m + 1)

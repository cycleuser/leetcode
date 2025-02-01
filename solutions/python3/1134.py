
class Solution:
    def isArmstrong(self, N: int) -> bool:
        # 将数字N转换为列表ns，其中每个元素为一个元组（当前位的值，该位的幂次）
        ns = [(int(c), 1) for c in str(N)]
        
        # 计算所有首位数之和
        sm = sum(a for a, _ in ns)
        
        # 当总和小于N时，更新ns中的数值并重新计算sm，直到sm >= N
        while sm < N:
            ns = [(a ** b, b) for a, b in ns]  # 更新每个数的幂次，并乘以原来的值
            sm = sum(a for a, _ in ns)
        
        # 检查更新后的总和是否等于N，是则为阿姆斯特朗数
        return sm == N

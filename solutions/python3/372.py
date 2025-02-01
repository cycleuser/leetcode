
class Solution:
    # 计算超幂，即计算 a 的 b 次方对 1337 取模的结果
    def superPow(self, a: int, b: list[int]) -> int:
        return pow(a, int(''.join(map(str, b))), 1337)  # 中文注释：将列表 b 转换为整数，计算 a 的 b 次方后对 1337 取模

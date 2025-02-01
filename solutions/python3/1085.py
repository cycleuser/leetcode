
class Solution:
    # 计算列表A中最小值的数字之和，并返回该和对2取反后的结果
    def sumOfDigits(self, A: List[int]) -> int:
        # 取出A中的最小值，转换为字符串，再将每个字符转换回整数并求和
        return 1 - (sum(map(int, str(min(A)))) % 2)  # Pythonic way using map and str functions

    # 计算列表A中最小值的数字之和，并返回该和对2取反后的结果
    def sumOfDigits(self, A: List[int]) -> int:
        min_num = min(A)
        # 将最小值转换为字符串，再将每个字符转换回整数并求和
        return 1 - (sum(int(c) for c in str(min_num)) % 2)  # Explicit way using generator expression


from functools import reduce
import math

# 判断一个数组中的所有整数是否可以通过某种组合方式使得它们的最大公约数为1
class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        # 使用reduce函数和math.gcd计算数组中所有元素的最大公约数，如果结果为1，则返回True，否则返回False
        return reduce(math.gcd, nums) == 1

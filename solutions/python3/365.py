
class Solution:
    # 定义一个求最大公约数的辅助函数
    def gcd(self, a, b):
        for i in range(min(a, b), 0, -1):  
            if not a % i and not b % i: 
                return i  

    # 主函数，判断给定的水箱容量x和y能否量出恰好z单位的水量
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        div = self.gcd(x, y) if x * y else 0  # 计算x和y的最大公约数div，特殊情况处理
        return not z % div and z <= x + y if div else not z  # 判断是否能量出恰好z单位的水量

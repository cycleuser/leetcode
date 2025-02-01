
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        # 将价格列表转换为浮点数
        # Convert the list of string prices to float
        prices = [float(p) for p in prices]

        # 计算所有整数部分之和
        # Calculate the sum of integer parts
        sm = sum(math.floor(p) for p in prices)

        # 将非零小数部分按从小到大排序
        # Sort non-zero fractional parts from smallest to largest
        prices = sorted([p - math.floor(p) for p in prices if p - math.floor(p)])

        # 如果整数部分之和大于目标值，或目标值与整数部分之和的差大于非零小数部分的数量，则返回-1
        # If the sum of integer parts is greater than the target, or the difference between the target and the sum of integer parts is greater than the number of non-zero fractional parts, return "-1"
        if sm > target or target - sm > len(prices):
            return "-1"

        # 计算需要调整的小数部分以达到目标值
        # Calculate the fractional parts to be adjusted to reach the target value
        return "{:.3f}".format(
            sum([p - math.floor(p) for p in prices[:sm - target]]) +
            sum([(math.ceil(p) - p) for p in prices[sm - target:]])
        )

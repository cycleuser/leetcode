
class Solution:
    # 判断一个数是否可以表示为两个平方数之和
    def judgeSquareSum(self, c: int) -> bool:
        # 遍历从0到根号c的所有可能值i
        for i in range(int(c ** 0.5) + 1):
            # 检查c - i**2 是否为完全平方数
            if not ((c - i ** 2) ** 0.5) % 1:
                return True
        return False

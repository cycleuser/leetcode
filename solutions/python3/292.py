
class Solution:
    # 判断给定的n是否能赢nim游戏（1到3步胜利）
    def canWinNim(self, n):
        """
        :type n: int  # 输入整数n，表示游戏中的石子数量
        :rtype: bool   # 返回布尔值，True表示可以获胜，False表示无法获胜
        """
        return False if n % 4 == 0 else True

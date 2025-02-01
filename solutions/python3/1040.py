
class Solution:
    # 定义一个类来解决石头移动问题

    def numMovesStonesII(self, A: List[int]) -> List[int]:
        """
        :param A: 石头的位置列表，整数类型
        :return: 两个元素的列表，分别表示最少和最多需要移动的次数
        """

        # 对石头位置进行排序
        A.sort()

        n = len(A)
        low, high = n, max(A[-1] - A[0] + 1 - n, A[-2] - A[1] + 1)

        # 初始化滑动窗口的左右边界，low表示最少移动次数，high表示最多移动次数
        i = 0

        # 滑动窗口右移，找到最少和最多的移动次数
        for j in range(n):
            while A[j] - A[i] >= n: 
                i += 1
            if j - i + 1 == n - 1 and A[j] - A[i] == n - 2:
                # 如果窗口内的石头数量为n-1且间隔正好为n-2，则最少移动次数为2
                low = min(low, 2)
            else:
                # 计算最少移动次数
                low = min(low, n - (j - i + 1))

        return [low, high]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        定义一个类，用于解决超级鸡蛋掉落问题。
        
        解释：
        - 通过动态规划方法计算在K个鸡蛋和N层楼的情况下最少需要尝试多少次才能确定鸡蛋的临界高度。
        """

        drops = 0                            # 记录鸡蛋被丢弃的数量
        floors = [0 for _ in range(K + 1)]   # floors[i] 表示使用 i 个鸡蛋可以检查的最大层数

        while floors[K] < N:                 # 当 K 个鸡蛋无法覆盖 N 层楼时继续循环
        
            # 对于每个鸡蛋数量 eggs，从 K 到 1 逆序遍历
            for eggs in range(K, 0, -1):
                # 更新 floors 数组中对应的值
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1

        return drops

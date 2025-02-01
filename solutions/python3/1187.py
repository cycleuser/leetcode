
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        arr1 和 arr2 是两个整数数组，我们需要对 arr1 进行操作使其变为严格递增序列。
        
        Parameters:
            - arr1: List[int] -- 第一个整数数组
            - arr2: List[int] -- 第二个整数数组

        Returns:
            int -- 返回将 arr1 变为严格递增序列所需的最小交换次数，如果无法变为递增序列则返回 -1。
        
        优化说明：
            - 使用 `defaultdict` 存储动态规划状态，并利用 `bisect` 模块进行二分查找加速操作
            - 将 `arr2` 排序以提高后续二分查找效率
        """
        dp = {-1: 0}  # 初始状态：-1 对应 0 次交换
        
        arr2.sort()  # 对 arr2 进行排序

        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))  # 初始化临时动态规划表
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])  # 当前元素直接继承上一状态的交换次数
                loc = bisect.bisect_right(arr2, key)  # 找到 arr2 中大于当前值的位置
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)  # 选择最优解更新临时表

            dp = tmp  # 更新动态规划状态

        if dp:
            return min(dp.values())  # 返回最小的交换次数
        return -1  # 若无法变为递增序列则返回 -1


class Solution:
    # 定义一个解决方案类

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        判断是否能在游戏中获胜
        
        :param maxChoosableInteger: 可选择的最大整数 (maxChoosableInteger)
        :param desiredTotal: 游戏目标分数 (desiredTotal)
        :return: 是否能赢得游戏 (bool)
        """
        
        # 如果所有可选数字之和小于目标分数，直接返回False
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        memo = {}  # 使用字典存储已经计算过的状态以避免重复计算
        
        def dfs(arr, total):
            """
            深度优先搜索函数
            
            :param arr: 当前可选择的数字列表 (list of int)
            :param total: 剩余需要达到的目标分数 (int)
            :return: 是否能在当前状态下获胜 (bool)
            """

            s = str(arr)  # 数组转字符串以便于字典键值
            if s in memo:
                return memo[s]  # 如果已经计算过此状态，直接返回结果

            if arr[-1] >= total:
                # 如果最后一个数字大于或等于剩余分数，则当前玩家获胜
                return True

            for i in range(len(arr)):
                # 尝试移除一个数字并检查对手是否能赢
                if not dfs(arr[:i] + arr[i+1:], total - arr[i]):
                    # 如果对手不能赢，记录当前状态为True（即自己可以赢）
                    memo[s] = True
                    return True

            # 如果所有尝试都无法让自己获胜，则记录当前状态为False
            memo[s] = False
            return False
        
        # 调用dfs函数并传入初始化的可选数字和目标分数
        return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal)

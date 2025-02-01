
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        """
        找出用最少步数匹配给定的字符串序列。
        
        参数:
            board (str): 给定的初始字符串序列，需要填充以匹配目标状态。
            hand (str): 可提供的字符，用于填充board。

        返回:
            int: 使用手头字符填充board所需最小步骤数量。如果无法完成任务返回-1。
        """

        def dfs(s: str, c: collections.Counter) -> int:
            """
            深度优先搜索，寻找匹配的最少步数。

            参数:
                s (str): 当前字符串状态。
                c (collections.Counter): 手头字符计数字典。

            返回:
                int: 从当前状态到目标状态所需的最小步骤数量。如果无法完成任务返回-1。
            """
            if not s: 
                return 0
            res, i = float("inf"), 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[i] == s[j]: 
                    j += 1
                incr = 3 - (j - i)
                if c[s[i]] >= incr:
                    incr = 0 if incr < 0 else incr
                    c[s[i]] -= incr
                    tep = dfs(s[:i] + s[j:], c)
                    if tep >= 0: 
                        res = min(res, tep + incr)
                    c[s[i]] += incr
                i = j
            return res if res != float("inf") else -1
        
        # 初始化手头字符计数字典
        hand_counter = collections.Counter(hand)
        return dfs(board, hand_counter)

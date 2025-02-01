
class Solution:
    # Python 解决旋转环与键的最小步骤问题

    def findRotateSteps(self, ring: str, key: str) -> int:
        # 用于存储字符在环中的位置索引
        index_dict = collections.defaultdict(list)
        n = len(ring)  # 环的长度
        dp = [0] * n  # 动态规划数组，记录到达每个位置的最小步骤数

        # 初始化: key的第一个字符在ring中对应的所有索引的位置，并计算初始步数
        for i, c in enumerate(ring):
            index_dict[c].append(i)
        for i in index_dict[key[0]]:
            dp[i] = min(i, n - i) + 1

        # 遍历key中的每个字符，更新dp数组和pre变量
        for c in key[1:]:
            pre = c  # 当前处理的字符
            for i in index_dict[c]:
                # 更新dp[i]为从上一个字符到当前字符所需的最小步骤数
                dp[i] = min(dp[j] + min(i - j, n + j - i) if i >= j else dp[j] + min(j - i, n + i - j) for j in index_dict[pre]) + 1

        # 返回最终结果，即key最后一个字符在环中对应位置的最小旋转步骤
        return min(dp[i] for i in index_dict[key[-1]])

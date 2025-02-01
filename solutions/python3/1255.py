
from collections import Counter as cnt


class Solution:
    # 定义深度优先搜索函数，用于递归寻找最大得分单词组合
    def maxScoreWords(self, w: List[str], l: List[int], s: List[int]) -> int:
        # 从给定的字母限制中计算初始使用情况
        use = cnt(l)
        
        # 定义深度优先搜索辅助函数
        def dfs(use, i):
            # 如果当前状态有效且未遍历完单词列表，则递归处理
            return (
                use and i < len(w) 
                and max(
                    dfs(use, i + 1),  # 不使用当前单词的情况
                    not cnt(w[i]) - use  # 检查当前单词是否可由剩余字母构成
                    and sum(s[ord(c) - ord("a")] for c in w[i])  # 计算当前单词得分
                    + dfs(use - cnt(w[i]), i + 1)  # 更新使用情况并递归处理下一个单词
                )
            )

        # 初始调用深度优先搜索，传入初始状态和起始索引0
        return int(dfs(use, 0))

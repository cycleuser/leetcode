
class Solution:
    """
    本题要求计算使得字符串s成为回文串的最小分割次数。
    中文注释：本题目标是求解将给定字符串s通过最少切割次数变成回文串。

    1. 使用优先队列存储当前起始位置和已经进行的切割次数。
    2. 遍历字符串，检查所有子串是否为回文。
    3. 如果是回文，则将结束位置加入字典中。
    4. 每次从队列中取出最小值，更新切割次数并继续处理。
    """

    def minCut(self, s: str) -> int:
        # 优先队列初始化
        q = [(0, 0)]
        # 回文子串字典
        pal = collections.defaultdict(list)
        used = {(0, 0)}

        # 遍历字符串，标记所有回文子串的结束位置
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    pal[i].append(j + 1)

        # 使用优先队列进行广度优先搜索
        while q:
            cuts, i = heapq.heappop(q)
            i *= -1

            # 当处理到字符串末尾时，返回当前切割次数减一（最后一刀不需要）
            if i == len(s): 
                return cuts - 1

            for j in pal[i]:
                if (cuts + 1, -j) not in used:
                    used.add((cuts + 1, -j))
                    heapq.heappush(q, (cuts + 1, -j))

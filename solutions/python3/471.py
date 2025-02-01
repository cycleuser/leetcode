
class Solution:
    def encode(self, s: str) -> str:
        """
        编码字符串，将其压缩为更短的形式。

        参数:
            s (str): 输入的原始字符串

        返回:
            str: 压缩后的字符串
        """

        def dfs(i, j):
            """
            深度优先搜索实现字符串编码。

            参数:
                i (int): 当前子串起始索引
                j (int): 当前子串结束索引

            返回:
                str: 编码后的子串
            """

            if i == j:
                return s[i]  # 如果是单个字符，直接返回

            if (i, j) not in memo:
                # 遍历所有分割点，寻找最短编码方式
                c1 = min((dfs(i, k) + dfs(k + 1, j)
                          if s[i:k + 1] != s[k + 1:j + 1]
                          else '2[' + dfs(i, k) + ']'
                          for k in range(i, j)),
                         key=len)

                c2 = s[i:j + 1]

                memo[(i, j)] = min(c1, c2, key=len)

                # 寻找重复子串并压缩
                for k in range(i, i + (j - i) // 2 + 1):
                    tar, ind, cnt = s[i:k + 1], i, 0
                    while ind + k - i <= j and s[ind:ind + k - i + 1] == tar:
                        cnt += 1
                        ind += k - i + 1

                    c3 = str(cnt) + '[' + tar + ']' + dfs(ind, j)
                    if ind <= j:
                        memo[(i, j)] = min(memo.get((i, j), ''), c3, key=len)

            return memo[(i, j)]

        memo = {}
        return dfs(0, len(s) - 1)

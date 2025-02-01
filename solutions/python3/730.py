
class Solution:
    # 定义一个解决类，用于计数回文子序列

    def countPalindromicSubsequences(self, S: str) -> int:
        # 设置模数和缓存字典以避免重复计算
        mod, memo = 10 ** 9 + 7, {}

        def dfs(i: int, j: int) -> int:
            # 如果子问题已经解决过，则直接返回结果
            if (i, j) not in memo:
                cnt = 0

                # 遍历'a', 'b', 'c', 'd'四个字符，尝试找到它们在当前子串中的位置
                for x in "abcd":
                    try:
                        # 找到第一个和最后一个x的位置
                        l, r = S[i:j + 1].index(x) + i, S[i:j + 1].rindex(x) + i

                        # 如果左右边界不同，说明有内部子序列，则递归计算中间部分的回文数并加2（包含边界）
                        if l != r:
                            cnt += dfs(l + 1, r - 1) + 2
                        else:
                            # 如果左右边界相同，直接计数+1
                            cnt += 1

                    except ValueError: 
                        # 没有找到对应字符时跳过此次迭代
                        continue

                memo[(i, j)] = cnt % mod
            
            return memo[(i, j)]

        # 从整个字符串的两端开始递归计算回文子序列数
        return dfs(0, len(S) - 1)

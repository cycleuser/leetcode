
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 使用字典 memo 存储已经计算过的状态，避免重复计算
        memo = {}

        def dfs(l, r, cnt):
            """
            :param l: 当前检查的左边界索引
            :param r: 当前检查的右边界索引
            :param cnt: 已经替换的字符个数
            :return: 是否可以通过至多一次删除变成回文串
            """

            # 如果当前状态已经计算过，直接返回结果
            if (l, r, cnt) in memo:
                return memo[(l, r, cnt)]

            # 如果左边界已经大于等于右边界，说明已经检查完一个完整区间
            if l >= r:
                return True

            # 当前字符不相等时，尝试删除一个字符并递归检查剩余部分
            elif s[l] != s[r]:
                cnt += 1
                # 如果已经超过一次替换，则直接返回 False
                if cnt > 1:
                    memo[(l, r, cnt)] = False
                    return False

                # 尝试两种删除方式：分别从左右两边删除一个字符并递归检查
                elif (s[l + 1] == s[r] and dfs(l + 1, r, cnt)) or (s[l] == s[r - 1] and dfs(l, r - 1, cnt)):
                    memo[(l, r, cnt)] = True
                    return True

                else:
                    # 如果两种删除方式都不成立，则返回 False
                    memo[(l, r, cnt)] = False
                    return False

            # 当前字符相等时，继续向内检查下一组字符
            else:
                memo[(l, r, cnt)] = dfs(l + 1, r - 1, cnt)
                return memo[(l, r, cnt)]

        # 从整个字符串的两端开始递归判断
        return dfs(0, len(s) - 1, 0)

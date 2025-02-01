
class Solution:
    # 定义一个类来解决平衡字符串分割问题

    def balancedStringSplit(self, s: str) -> int:
        # 初始化结果计数器res和当前平衡计数器cnt为0
        res = cnt = 0
        # 遍历输入字符串s中的每一个字符c
        for c in s:
            # 如果字符c是'L'，增加当前平衡计数器cnt
            if c == 'L':
                cnt += 1
            # 如果字符c是'R'，减少当前平衡计数器cnt
            elif c == 'R':
                cnt -= 1
            # 当当前平衡计数器cnt为0时，说明找到了一个平衡的子字符串，结果计数器res加一
            if cnt == 0:
                res += 1
        # 返回最终的结果计数器res，表示平衡子字符串的数量
        return res

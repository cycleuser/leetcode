
class Solution:
    # 定义一个类来解决字符串子串问题

    def equalSubstring(self, s: str, t: str, mx: int) -> int:
        i = 0
        # 初始化滑动窗口的左边界为0
        for j in range(len(s)):
            # 计算当前字符对之间的绝对差值，并从mx中减去
            mx -= abs(ord(s[j]) - ord(t[j]))
            if mx < 0:
                # 如果剩余的最大可承受差值小于0，说明需要缩小窗口左边界
                # 所以恢复对应的mx的消耗，并移动左边界
                mx += abs(ord(s[i]) - ord(t[i]))
                i += 1
        # 返回满足条件的子串的最大长度
        return j - i + 1

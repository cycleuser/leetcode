
class Solution:
    # 判断typed字符串是否为name的长按变形
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pre = None  # 前一个字符
        i = 0       # name字符串索引

        for c in typed:
            # 如果当前typed中的字符与name当前字符相同，更新前一个字符和i的位置
            if i < len(name) and c == name[i]:
                pre, i = name[i], i + 1
            # 否则如果当前typed中的字符与pre不同，则返回False
            elif c != pre:
                return False

        # 检查是否遍历完name字符串
        return i == len(name)

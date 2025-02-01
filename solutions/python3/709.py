
class Solution:
    # 将字符串中的大写字母转换为小写，保持其他字符不变
    def toLowerCase(self, str):
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)

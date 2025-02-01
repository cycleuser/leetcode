
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        :param s: 输入字符串
        :return: 反转单词后的字符串
        """
        j, s_out = 0, ""
        for i, char in enumerate(s):
            # 如果是最后一个字符，处理剩余部分并返回结果
            if i == len(s) - 1:
                s_out += s[j:i + 1][::-1]
                return "".join(s_out)
            # 遇到空格，处理当前单词，并重置起始位置
            if char == " ":
                s_out += s[j:i][::-1] + " "
                j = i + 1
        # 返回最终结果
        return "".join(s_out)

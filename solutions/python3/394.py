
class Solution:
    def decodeString(self, s):
        """
        解码字符串的实现。使用栈来帮助处理嵌套的括号结构。
        
        参数:
        s (str): 输入的编码字符串
        
        返回值:
        str: 解码后的字符串
        """
        stack, num, string = [], 0, ""
        for c in s:
            # 遇到左括号时，将当前累积的数和字符串压入栈中，并重置它们
            if c == "[":
                stack += (string, ),
                stack += (num, )
                num, string = 0, ""
            # 遇到右括号时，从栈中弹出上一个数和字符串，并更新当前的解码结果
            elif c == "]":
                pre_num, pre_string = stack.pop(), stack.pop()
                string = pre_string + pre_num * string
            # 当前字符是数字时，构建数字
            elif c.isdigit():
                num = num * 10 + int(c)
            # 其他情况下直接拼接当前字符
            else:
                string += c
        return string

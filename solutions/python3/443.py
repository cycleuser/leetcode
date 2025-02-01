
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        curr, count, i = chars[0], 1, 1  # 当前字符，计数器，索引

        while i < len(chars):
            if chars[i] != curr:
                # 当遇到不同字符时，处理当前字符和计数
                curr = chars[i]
                if count > 1: 
                    # 如果有多个相同的字符，则插入计数字符到列表中
                    chars[:i] += ''.join(str(count))
                    i += len(str(count))  # 跳过已添加的计数字符

            else:
                # 继续增加相同字符的计数，直到遇到不同字符
                if i == len(chars) - 1: 
                    # 如果是最后一个相同的字符，则更新并退出循环
                    chars.pop(i)
                    chars += ''.join(str(count + 1))
                    break
                chars.pop(i)  # 移除当前字符
                count += 1

            i += 1  # 增加索引值

        return len(chars)  # 返回压缩后的字符串长度

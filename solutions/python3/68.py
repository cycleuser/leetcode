
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        解决方案类，包含全对齐文本的实现。
        
        :param words: 一个字符串列表，表示单词列表
        :param maxWidth: 整数，表示每一行的最大宽度
        :return: 返回格式化后的字符串列表
        """
        res, used, s = [], 0, []
        
        # 遍历每一个单词
        for i, w in enumerate(words):
            if not s or len(w) + used + len(s) <= maxWidth:
                # 当前行还可以容纳当前单词，则添加到当前行中
                used += len(w)
                s += [w]
            else:
                # 如果当前行已满，处理当前行内容，并重置用于下一行
                if len(s) == 1:
                    res.append(s[0] + (maxWidth - used) * ' ')
                else:
                    br = (maxWidth - used) // (len(s) - 1)
                    # 计算空格数，分配到各单词间
                    res.append(''.join((br + (i <= (maxWidth - used) % (len(s) - 1))) * ' ' + c for i, c in enumerate(s)).lstrip())
                used, s = len(w), [w]
        
        # 处理最后一行左对齐且尾部填充空格
        return res + [' '.join(c for c in s) + (maxWidth - used - len(s) + 1) * ' ']

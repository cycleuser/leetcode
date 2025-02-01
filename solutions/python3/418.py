
class Solution:
    # 定义一个类来解决单词排版问题

    def wordsTyping(self, sentence, rows, cols):
        # 初始化一些变量，用于记录每个单词的起始位置、当前行的剩余空格数、当前指针位置和单个单词长度
        left, count, sm, ptr, wordLen = [0] * len(sentence), 0, 0, 0, len(sentence[0])
        
        # 遍历每个单词，计算每个单词在一行中占据的空间
        for i, w in enumerate(sentence):
            while sm + wordLen <= cols:
                sm += wordLen  # 当前指针指向的单词长度加到剩余空格数上
                ptr += 1       # 指针右移一个位置
                wordLen = len(sentence[ptr % len(sentence)]) + 1  # 更新下一个单词的长度
        
            left[i] = ptr - i  # 记录当前单词开始的位置
            sm -= len(w) + 1   # 减去当前单词和空格，为下次计算做准备
        
        # 遍历行数，累加每个单词的起始位置信息
        for r in range(rows):
            count += left[count % len(sentence)]
        
        return count // len(sentence)  # 返回最终结果

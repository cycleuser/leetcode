
class Solution:
    # 定义一个解决方案类，用于解决最小编码长度问题

    def minimumLengthEncoding(self, words):
        """
        :type words: List[str] - 输入单词列表
        :rtype: int - 返回最短的编码长度
        
        思路：使用集合去重，并通过遍历每个单词的所有子串来进一步去除冗余，最终计算剩余字符串的总长度加一。
        """
        s = set(words)
        # 将输入的单词列表转换为一个集合以移除重复项

        for word in words:
            for i in range(1, len(word)):
                # 遍历每个单词的所有子串（从第二个字符开始）
                s.discard(word[i:])
                # 从当前单词的子串在集合中删除，确保没有冗余
        return sum(len(w) + 1 for w in s)
        # 返回剩余字符串总长度加一之和

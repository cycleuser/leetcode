
class Solution:
    # 中文: 定义一个Solution类，包含wordsAbbreviation方法来处理词组缩写。
    # 英文: Define a Solution class with the wordsAbbreviation method to handle word abbreviations.

    def wordsAbbreviation(self, dict):
        abb = collections.defaultdict(int)  # 中文: 使用defaultdict统计每个缩写的出现次数。英文: Use defaultdict to count occurrences of each abbreviation.
        
        for i, w in enumerate(dict):  # 中文: 遍历字典中的每一个词。英文: Iterate through the dictionary and its words.
            for j in range(1, len(w) - 2):
                abb[w[:j] + str(len(w) - j - 1) + w[-1]] += 1  # 中文: 构造缩写并统计出现次数。英文: Construct abbreviation and count occurrences.

        for i, w in enumerate(dict):  # 中文: 再次遍历字典中的每一个词。英文: Iterate through the dictionary again.
            for j in range(1, len(w) - 2):
                new = w[:j] + str(len(w) - j - 1) + w[-1]
                if abb[new] == 1:  # 中文: 判断缩写出现次数是否为1。英文: Check if the abbreviation's count is 1.
                    dict[i] = new
                    break  # 中文: 如果是，则更新词组并跳出循环。英文: Update the word and break out of the loop.

        return dict  # 中文: 返回处理后的字典。英文: Return the processed dictionary.


class Solution:
    # 中文注释：实现 indexPairs 方法，输入为字符串 text 和单词列表 words，
    # 输出所有可能的 [起始索引, 结束索引] 对，使得 text 的子串等于 words 中的一个单词。
    # 英文注释: Implement the indexPairs method which takes a string 'text' and a list of strings 'words',
    # and returns all possible [start_index, end_index] pairs such that the substring in 'text' equals one of the words in 'words'.
    
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # 中文注释：使用列表推导式生成所有可能的子串索引对
        # 英文注释: Use list comprehension to generate all possible substring index pairs.
        return [[i, j] for i in range(len(text)) 
                for j in range(i, len(text)) if text[i:j + 1] in words]

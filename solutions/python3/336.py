
class Solution:
    def palindromePairs(self, words):
        """
        中文注释：构建一个映射，将单词及其索引对应起来。
        英文注释: Build a mapping to associate each word with its index.
        """
        index, res = {w:i for i, w in enumerate(words)}, []
        
        """
        中文注释：遍历每个单词，并将其拆分为前后两部分，检查前半部分是否为回文。
        英文注释: Iterate over each word and split it into two parts. Check if the first part is a palindrome.
        """
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                pre, suf = w[:j], w[j:]
                
                """
                中文注释：如果前半部分是回文，反转后半部分并检查是否在字典中且不等于原单词。
                英文注释: If the first part is a palindrome, reverse the second part and check if it exists in the dictionary and is not equal to the original word.
                """
                if pre == pre[::-1]:
                    suf = suf[::-1]
                    if suf != w and suf in index:
                        res.append([index[suf], i])
                
                """
                中文注释：检查后半部分是否为回文，如果不是开头部分，则反转前半部分并检查是否在字典中。
                英文注释: Check if the second part is a palindrome, and if not the first part, reverse the first part and check if it exists in the dictionary.
                """
                if j != len(w) and suf == suf[::-1]:
                    pre = pre[::-1]
                    if pre != w and pre in index:
                        res.append([i, index[pre]])
        
        return res

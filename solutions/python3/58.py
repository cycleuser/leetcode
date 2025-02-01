
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        :param s: 输入字符串
        :return: 最后一个单词的长度
        """
        if len(s) == 0:
            # 如果输入为空字符串，返回0
            return 0
        
        count = 0
        prev_count = 0
        
        for letter in s:
            # 如果当前计数大于0，记录前一个计数值
            if count > 0:
                prev_count = count
            
            # 遇到空格时重置计数并跳过该循环迭代
            if letter == " ":
                count = 0
                continue
            
            count += 1
        
        # 如果最后一个单词长度大于0，返回其长度；否则返回前一个计数值
        if count > 0:
            return count
        else:
            return prev_count

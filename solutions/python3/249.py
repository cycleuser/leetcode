
import collections

class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # 使用字典存储相同模式的字符串列表
        # defaultdict自动处理不存在键的情况，避免None检查
        table = collections.defaultdict(list)
        
        for w in strings:
            pattern = ""
            # 遍历单词中的每个字符（从第二个开始）
            for i in range(1, len(w)):
                # 计算两个连续字符之间的差值，并转换为模式字符串
                if ord(w[i]) - ord(w[i - 1]) >= 0:
                    pattern += str(ord(w[i]) - ord(w[i - 1]))
                else:
                    pattern += str(ord(w[i]) - ord(w[i - 1]) + 26)
            
            # 根据计算出的模式字符串将当前单词添加到字典中对应的列表
            table[pattern].append(w)
        
        # 返回所有具有相同模式字符串的列表
        return [table[pattern] for pattern in table]

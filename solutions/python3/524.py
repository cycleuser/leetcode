
class Solution:
    # 定义一个类来解决寻找字符串中包含的最长词的问题
    
    def findLongestWord(self, s: str, d: list[str]) -> str:
        # 对字典d中的单词按长度降序排序，如果长度相同则按字典序升序
        d.sort(key=lambda x: (-len(x), x))
        
        # 遍历排序后的列表中的每个单词
        for w in d:
            i = 0  # 初始化指针i指向s的当前比较位置
            for c in s:
                if c == w[i]: 
                    i += 1  # 如果s中的字符与w中的匹配，移动指针i
                if i == len(w):  # 如果整个单词都匹配完成
                    return w  # 返回该单词
        
        return ""  # 如果没有找到匹配的最长词，则返回空字符串

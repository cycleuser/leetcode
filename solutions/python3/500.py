
class Solution:
    """
    中文注释: 
    定义一个解决方案类，包含一个方法用于查找满足特定条件的单词。
    
    English comments:
    Define a solution class containing a method to find words that meet specific conditions.
    """

    def findWords(self, words):
        """
        中文注释: 
        该函数接收一个单词列表作为参数，返回其中只包含英文字母表三行中任意一行的字母的单词。

        English comments:
        This function accepts a list of words as an argument and returns the words that only contain letters from any one of the three rows of the QWERTY keyboard.
        """
        
        # 定义键盘三行字母集合
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        
        # 过滤并返回符合条件的单词列表
        return [
            w 
            for w in words 
            if any(
                not (set(w.lower()) - row)  # 检查当前单词的小写形式是否完全包含在某一行中
                for row in rows
            )
        ]

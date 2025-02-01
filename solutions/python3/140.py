
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """
        判断字符串s是否可以被wordDict中的单词分割，并返回所有可能的分割方式。
        
        参数:
            s (str): 待分割的字符串
            wordDict (list[str]): 单词列表

        返回:
            list[str]: 所有可能的分割结果
        """

        def breakable():
            """
            判断给定字符串是否可被字典中的单词分割。

            返回:
                bool: 是否可以分割
            """
            rightmosts = [0]
            for i in range(1, len(s) + 1):
                for last_index in rightmosts:
                    if s[last_index:i] in words:
                        rightmosts.append(i)
                        if i == len(s): 
                            return True
                        break
            return False
        
        # 使用队列进行广度优先搜索
        q, res, words = [("", 0)], [], set(wordDict)
        
        if breakable():
            for j in range(1, len(s) + 1):
                new = q[:]
                for seq, i in q:
                    if s[i:j] in words:
                        if j == len(s):
                            res.append(seq and seq + " " + s[i:j] or s[i:j])
                        else:
                            new.append((seq and seq + " " + s[i:j] or s[i:j], j))
                q = new

        return res

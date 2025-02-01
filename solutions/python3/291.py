
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        """
        判断给定的模式 pattern 是否可以匹配字符串 s。
        
        :param pattern: 字符串，表示模式
        :param s: 字符串，待匹配的目标字符串
        :return: 如果存在一种一一对应关系使得 pattern 能完全匹配 s，则返回 True
        
        例如:
        pattern = "abab", s = "redblueredblue" -> True (a -> red, b -> blue)
                pattern = "aaaa", s = "asdasdasdasd" -> False (无法找到满足条件的映射关系)
        """
        
        def dfs(i: int, j: int, dic: dict, used: set) -> bool:
            """
            深度优先搜索，递归地检查 pattern 是否能匹配 s。
            
            :param i: 当前处理到 pattern 中的第几个字符
            :param j: 当前处理到字符串 s 中的起始位置
            :param dic: 已经确定好的字符 -> 子串 映射关系字典
            :param used: 已经使用的子串集合，防止重复使用同一个子串
            
            返回值：
                如果存在一种匹配方式使得 pattern[i:] 能完全匹配 s[j:], 则返回 True 
            """
            
            if i >= len(pattern) or j >= len(s):
                # 模式遍历完或字符串遍历完且相等才成立
                return i == len(pattern) and j == len(s)
            elif pattern[i] in dic:
                # 当前字符已经匹配过，检查是否能继续匹配
                return s[j:j + len(dic[pattern[i]])] == dic[pattern[i]] and dfs(i + 1, j + len(dic[pattern[i]]), dic, used)
            else:
                for k in range(j + 1, len(s) + 1):
                    # 尝试所有可能的子串
                    if s[j:k] not in used:
                        dic[pattern[i]] = s[j:k]
                        if dfs(i + 1, j + len(dic[pattern[i]]), dic, used | {s[j:k]}):
                            return True
                        # 恢复现场，回溯检查其他可能的子串
                        dic.pop(pattern[i])
                return False

        return dfs(0, 0, {}, set())

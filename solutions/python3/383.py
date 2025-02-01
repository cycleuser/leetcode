
class Solution:
    # 判断ransomNote是否可以通过magazine中的字符按顺序拼接而成
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter  # 导入计数器类

        cnt = Counter(magazine)  # 统计magazine中每个字符的出现次数
        
        for c in ransomNote:
            if cnt[c]:  # 如果字符c在magazine中有剩余
                cnt[c] -= 1  # 使用一个字符，计数减一
            else:  # 没有剩余
                return False  # 返回False

        return True  # 所需字符都可用，返回True

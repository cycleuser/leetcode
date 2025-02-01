
from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        # 统计字符串s中每个字符出现的次数，使用Counter进行统计
        cnt = Counter(s)
        
        # 计算字符串长度的一半
        n = len(s) // 2
        
        # 找出所有出现奇数次的字符
        odd = [c for c in cnt if cnt[c] % 2]
        
        # 构建初始中间部分，使用'#'填充
        s = "".join(k * (cnt[k] // 2) for k in cnt)
        q = {"#" * n}
        
        # 如果出现奇数次的字符超过一个，则无法构成回文串
        if len(odd) > 1:
            return []
        
        # 遍历当前已有的字符串组合
        for c in s:
            new = set()
            
            # 对于每个已有字符串，插入新的字符c生成新字符串
            for w in q:
                for i in range(n):
                    if w[i] == "#":
                        new.add(w[:i] + c + w[i + 1:])
            
            # 更新当前的已有的字符串组合
            q = new
        
        # 根据出现奇数次的字符生成最终回文串
        return [w + odd[0] + w[::-1]] if odd else [w + w[::-1] for w in q]

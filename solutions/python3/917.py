
class Solution:
    # 1. 初始化解决方案类

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        # 2. 输入：字符串S；输出：经过处理的字符串
        """
        
        r = [s for s in S if s.isalpha()]
        # 3. 使用列表推导式筛选出所有字母
        
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))
        # 4. 遍历原字符串S，如果是非字母字符保持不变；若是字母则替换为r中的最后一个字母，并从r中移除该字母

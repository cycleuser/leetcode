
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        移除无效的括号，使字符串合法。该函数会返回所有可能的结果。
        
        Args:
            s (str): 输入的包含字母和括号的字符串
        
        Returns:
            List[str]: 一个列表，其中包含所有移除了无效括号后的合法字符串
        """
        
        l = r = 0
        # 计算需要移除的左括号和右括号数量
        for c in s:
            if c.isalpha(): 
                continue
            if c == "(": 
                l += 1 
            elif l: 
                l -= 1 
            else: 
                r += 1 
        
        q = {("", l, r, 0, 0)}
        # 使用集合模拟队列，存储状态 (字符串, 需移除的左括号数, 需移除的右括号数, 当前左括号计数, 当前右括号计数)
        
        for c in s:
            new = set()
            # 生成新的状态集合
            for st, l, r, lCur, rCur in q:
                if c == "(":
                    new.add((st + c, l, r, lCur + 1, rCur))
                    if l: 
                        new.add((st, l - 1, r, lCur, rCur))
                elif c == ")":
                    if lCur: 
                        new.add((st + c, l, r, lCur - 1, rCur))
                    else: 
                        new.add((st + c, l, r, lCur, rCur + 1))
                    if r: 
                        new.add((st, l, r - 1, lCur, rCur))
                else:
                    new.add((st + c, l, r, lCur, rCur))
            q = new
        # 更新状态集合
        
        return list({st for st, l, r, lCur, rCur in q if l == r == lCur == rCur == 0})
        # 返回所有满足条件的合法字符串列表

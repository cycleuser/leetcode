
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # 初始化栈和结果集，当前集合
        stack, res, cur = [], [], []
        
        for i in range(len(expression)):
            v = expression[i]
            
            # 当前字符为字母时，将当前字符加入所有已有子集
            if v.isalpha():
                cur = [c + v for c in cur or ['']]
            
            # 左括号出现时，压入结果和当前集合到栈中，并初始化新集合
            elif v == '{':
                stack.append(res)
                stack.append(cur)
                res, cur = [], []
            
            # 右括号出现时，弹出上一个集合和结果集拼接当前子集后再次放入结果集中
            elif v == '}':
                pre = stack.pop()
                preRes = stack.pop()
                cur = [p + c for c in res + cur for p in pre or ['']]
                res = preRes
            
            # 逗号出现时，将当前集合加入结果集并清空当前集合
            elif v == ',':
                res += cur
                cur = []
        
        return sorted(set(res + cur))


class Solution:
    # 判断字符串s中的括号是否有效，即所有左括号都有对应的右括号且顺序正确
    
    def isValid(self, s: str) -> bool:
        # 初始化栈和左右括号集合
        brackets_stack = []
        lefts, rights = ("(", "[", "{"), (")", "]", "}")
        
        for char in s:
            # 如果当前字符是左括号，入栈
            if char in lefts: 
                brackets_stack.append(char)
            elif not brackets_stack or lefts.index(brackets_stack.pop()) != rights.index(char): 
                # 如果当前字符是右括号且不匹配或栈为空则返回False
                return False
        
        # 栈为空表示所有左括号都有对应的右括号且顺序正确，返回True
        return not brackets_stack

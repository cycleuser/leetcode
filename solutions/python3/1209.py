
class Solution:
    # 定义一个类来解决去重问题

    def removeDuplicates(self, s: str, k: int) -> str:
        # 初始化栈，用于记录字符及其出现次数
        stack = []
        
        for i, c in enumerate(s):
            # 如果栈为空或当前字符与栈顶字符不同，则入栈
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                # 否则，更新栈顶字符的计数
                stack[-1][1] += 1
            
            # 如果当前字符重复次数达到k次，则弹出该字符记录
            if stack and stack[-1][1] == k:
                stack.pop()
        
        # 最终结果通过拼接栈中字符及其出现次数生成
        return ''.join(k * v for k, v in stack)

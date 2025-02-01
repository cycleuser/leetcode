
class Solution:
    # 定义一个类，用于处理括号序列并计算深度划分

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []  # 使用栈来跟踪左括号的位置
        res = [0] * len(seq)  # 初始化结果列表，长度与输入相同
        
        for i, c in enumerate(seq):
            # 遇到左括号时，将其索引压入栈中，并决定是否使用正负值标记
            if c == '(':
                stack.append(i if not stack or stack[-1] < 0 else -i)
            else:
                # 遇到右括号时，弹出对应的左括号索引
                ind = stack.pop()
                if ind >= 0:  # 如果索引为正数，则表示之前也是左括号
                    res[i] = res[ind] = 1  # 标记这对括号需要进行深度划分
        
        return res  # 返回结果列表，表示每个字符是否需要深度划分

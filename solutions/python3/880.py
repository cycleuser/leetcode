
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        """
        解码字符串S中的第K个字符。
        
        参数:
            S (str): 输入的编码字符串
            K (int): 需要找到的解码后位置
        
        返回:
            str: 第K个解码后的字符
        """

        stack, l = [], 0
        # 遍历字符串S中的每个字符c
        for c in S:
            # 如果是字母，长度加1；如果是数字，则扩展当前的总长度l
            l += 1 if c.isalpha() else int(c) * l
            stack.append(c)
            # 当累积长度大于等于K时开始回溯处理
            while l >= K:
                # 弹出栈顶元素，更新长度l
                while isinstance(stack[-1], int):
                    l //= stack.pop()
                # 更新K的位置，并判断是否找到解码结果
                K %= l
                if not K: return stack[-1]
                l -= 1
                stack.pop()

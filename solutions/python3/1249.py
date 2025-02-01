
class Solution:
    # 初始化解决方案类

    def minRemoveToMakeValid(self, s: str, res: str = "", l: str = "(", r: str = ")", b: int = 0) -> str:
        # 方法：移除最少的字符以使字符串有效（中英文双语注释）
        
        for _ in range(2):  # 循环两次，第一次正序处理，第二次逆序处理
            for c in s:  # 遍历字符串s中的每个字符c
                if c == r and b <= 0:
                    continue  # 如果当前字符是右括号且剩余的左括号数为零，则跳过
                b += c == l  # 当前字符是左括号时，增加剩余左括号数量b
                b -= c == r  # 当前字符是右括号时，减少剩余左括号数量b
                res += c  # 将当前字符添加到结果字符串res中

            # 重置状态变量并逆序处理字符串s
            res, s, l, r, b = "", res[::-1], r, l, 0
        
        return s  # 返回最终的有效字符串

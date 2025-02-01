
class Solution:
    # 初始化方法，无参数，用于实例化Solution类

    def removeOuterParentheses(self, S: str) -> str:
        """
        移除字符串S最外层的括号。
        
        参数:
            S (str): 输入的字符串，包含有效的括号序列
        
        返回:
            str: 去掉最外层括号后的结果
        """
        l = r = 0  # 初始化左括号和右括号计数器
        res = cur = ''  # 初始化结果字符串和当前子串

        for s in S:
            cur += s  # 将当前字符加入当前子串中
            if s == '(': l += 1  # 左括号计数加一
            elif s == ')': r += 1  # 右括号计数加一

            # 当左括号和右括号数量相等时，说明找到了一个完整的子串
            if l == r:
                res += cur[1:-1]  # 将当前子串去掉首尾后的部分加入结果字符串中
                cur = ''  # 清空当前子串

        return res  # 返回最终结果字符串

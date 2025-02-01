
class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 使用两个栈分别存储左括号和星号的位置信息，方便后续匹配
        # Chinese: 使用两个栈分别存储左括号和星号的位置信息，方便后续匹配
        left, left_star = [], []
        
        for i in range(len(s)):
            if s[i] == "(":  # 遇到左括号时记录其位置
                # Chinese: 遇到左括号时记录其位置
                left.append([s[i], i])
            elif s[i] == "*":  # 遇到星号时记录其位置
                # Chinese: 遇到星号时记录其位置
                left_star.append([s[i], i])
            elif left and left[-1][0] == "(":  # 如果当前是右括号且栈顶元素为左括号，匹配成功出栈
                # Chinese: 如果当前是右括号且栈顶元素为左括号，匹配成功出栈
                left.pop()
            elif left_star:  # 使用星号进行匹配
                # Chinese: 使用星号进行匹配
                left_star.pop()
            else:
                return False
        
        # 处理剩余未匹配的左括号和星号
        while left and left_star and left[-1][1] < left_star[-1][1]:  # 确保星号在左括号之后用于填充
            # Chinese: 处理剩余未匹配的左括号和星号，确保星号在左括号之后用于填充
            left.pop(); left_star.pop()
        
        return not left  # 如果所有左括号都被匹配，则返回True

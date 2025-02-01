
class Solution:
    def solveEquation(self, equation):
        """
        解决一元一次方程问题
        
        :param equation: 代表方程的字符串，格式如 "x+5-3+x=6+x-2"
        """

        def calc(eq):
            """
            计算表达式中的x系数和常数项
            
            :param eq: 字符串形式的一元一次方程部分
            :return: x系数与常数项组成的元组
            """
            smX = smNum = 0
            add, num = True, ""
            for c in eq + "+":
                if c.isdigit():
                    num += c
                elif c == "x":
                    smX += int(num) if add and num else -int(num) if num else 1 if add else -1
                    num = ""
                else:
                    smNum += int(num) if add and num else -int(num) if num else 0
                    num, add = "", c == "+"
            return smX, smNum

        # 分割等号左右两边的表达式
        eq = equation.split("=")
        lX, lNum, rX, rNum = calc(eq[0]) + calc(eq[1])

        if lX == rX:
            return "No solution" if lNum != rNum else "Infinite solutions"

        # 计算x的值
        return f"x={str((lNum - rNum) // (rX - lX))}"

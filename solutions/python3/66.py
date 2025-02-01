
class Solution:
    # 定义一个类Solution，用于处理数字加一的问题

    def plusOne(self, digits, add=1):
        # 定义一个方法plusOne，接收参数digits（数字列表）和add默认值为1

        return [1] if not digits and add else []  # 如果digits为空且add不为0，则返回[1]
        
        # 递归处理剩余的数字
        return self.plusOne(digits[:-1], +(digits[-1] + add > 9)) + [(digits[-1] + add) % 10]

        # 优化：使用条件表达式简化代码逻辑
        return [1] if not digits else (self.plusOne(digits[:-1], +(digits[-1] + add > 9)) + 
                                      [(digits[-1] + add) % 10])


class Solution:
    # 计算两个数按照指定操作符进行计算的结果
    def calc(self, l, op, r):
        # 中文注释: 根据操作符执行加减乘运算并返回结果
        return l + r if op == "+" else l - r if op == "-" else l * r

    # 生成所有可能的计算方式，输入为表达式字符串
    def diffWaysToCompute(self, input):
        # 中文注释: 如果输入是一个数字直接返回该数字
        if input.isdigit():
            return [int(input)]
        
        res = []
        # 遍历整个输入字符串
        for i in range(len(input)):
            # 检查当前字符是否为运算符
            if input[i] in "-+*":
                # 分别递归计算左右子表达式的所有可能结果
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i + 1:])
                
                # 将当前运算符应用到所有组合的结果中
                for j in l:
                    for k in r:
                        res.append(self.calc(j, input[i], k))
        
        return res

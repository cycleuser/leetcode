
class Solution:
    def __init__(self):
        # 初始化小于20、十位数和千位数的单词列表
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
                           "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                           "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        # 如果输入数字为0，直接返回"Zero"
        if not num:
            return "Zero"

        res = ""
        
        # 遍历千位数数组
        for i in range(len(self.thousands)):
            if num % 1000:
                # 处理当前千位数部分的数字并添加对应单位词，然后加到结果字符串前部
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000

        return res.strip()

    def helper(self, num):
        # 如果输入数字为0，直接返回空字符串
        if not num:
            return ""
        
        # 小于20的数字转换
        elif num < 20:
            return self.lessThan20[num] + " "

        # 处理10到99之间的数
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)

        else:  # 大于等于100
            return self.lessThan20[num // 100] + " Hundred " + self.helper(num % 100)


class Solution:
    def intToRoman(self, num: int) -> str:
        # 将千位数转换为罗马数字
        s = "M" * (num // 1000)
        
        # 处理百位数，考虑特殊情况900和400
        if num % 1000 >= 900:
            s += "CM"
        else:
            s += "D" * ((num % 1000) // 500)
        
        # 处理剩余的百位数，考虑特殊情况400和300
        if num % 500 >= 400 and s[-2:] != "CM":
            s += "CD"
        else:
            s += "C" * ((num % 500) // 100)
        
        # 处理剩余的十位数，考虑特殊情况90和40
        if num % 100 >= 90:
            s += "XC"
        else:
            s += "L" * ((num % 100) // 50)
        
        # 处理剩余的个位数，考虑特殊情况40和30
        if num % 50 >= 40 and s[-2:] != "XC":
            s += "XL"
        else:
            s += "X" * ((num % 50) // 10)
        
        # 处理个位数，考虑特殊情况9和4
        if num % 10 >= 9:
            s += "IX"
        else:
            s += "V" * ((num % 10) // 5)
        
        # 处理剩余的个位数，考虑特殊情况4
        if num % 5 >= 4 and s[-2:] != "IX":
            s += "IV"
        else:
            s += "I" * (num % 5)
        
        return s

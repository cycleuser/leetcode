
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int  # 输入的整数
        :rtype: bool     # 返回是否为完数（真则返回True，假则返回False）
        
        检查给定整数是否为完数。
        完数定义：一个正整数等于其所有正因子之和减去它本身。
        """
        sm, div = 1, 2
        # 循环条件：当前因子的平方小于或等于num，以减少不必要的计算
        while div ** 2 <= num:
            if num % div == 0: 
                sm += div + (num // div)  # 添加所有因子到总和中
            div += 1
        return sm == num and div > 2  # 判断是否为完数，并确保至少有两个因子（排除1）

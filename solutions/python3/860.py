
class Solution:
    def lemonadeChange(self, bills):
        # 定义5元和10元硬币的数量
        five = ten = 0
        
        for num in bills:
            # 如果收到的是5元
            if num == 5:
                five += 1
            # 如果收到的是10元且有5元可用
            elif num == 10 and five:
                ten += 1
                five -= 1
            # 如果收到的是20元且有5元和10元都可用
            elif num == 20 and five and ten:
                five -= 1
                ten -= 1
            # 如果收到的20元且仅有足够的5元
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        
        # 如果所有情况都满足，则返回True
        return True

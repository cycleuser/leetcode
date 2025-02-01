
class Solution:
    # 定义一个类来解决问题
    
    def numRabbits(self, answers):
        # 初始化字典和结果计数器
        dic, res = {}, 0
        
        for ans in answers:
            # 如果答案不在字典中，或者字典中的值大于当前答案，则更新字典并增加结果计数值
            if ans not in dic or dic[ans] > ans:
                dic[ans] = 1
                res += ans + 1
            else:
                # 否则，只增加字典对应的值
                dic[ans] += 1
        
        return res  # 返回最终结果

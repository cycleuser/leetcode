
class Solution:
    # 判断给定的数字列表是否可以通过加、减、乘、除得到接近24的结果
    
    def judgePoint24(self, nums):
        from collections import deque
        
        # 初始化队列，每个元素是一个操作后的数对和剩余未处理的数列表
        q = deque([[None, nums[i]] + nums[:i] + nums[i + 1:] for i in range(len(nums))])
        
        while q:
            new = []
            
            # 遍历当前队列中的每个元素
            for group1, group2, *rest in q:
                if not rest and group1:  # 如果剩余列表为空且第一个数非空，尝试四则运算
                    for res in (group1 + group2, group1 - group2, group1 * group2, group2 and group1 / group2):
                        if 23.999 <= res <= 24.0001: 
                            return True
                
                if not rest and not group1 and 23.999 <= group2 <= 24.0001:  # 如果剩余列表为空且第一个数非空，直接返回True
                    return True
                
                for i in range(len(rest)):
                    # 处理剩余列表中的每个数字与group2的四则运算
                    for newGroup2 in (group2 + rest[i], group2 - rest[i], rest[i] - group2, group2 * rest[i], group2 / rest[i]):
                        new.append([group1, newGroup2] + rest[:i] + rest[i + 1:])
                    
                    if group2:
                        # 处理剩余列表中的每个数字与除法
                        new.append([group1, rest[i] / group2] + rest[:i] + rest[i + 1:])
                    
                    if group1 is not None:
                        for newGroup1 in (group1 + group2, group1 - group2, group1 * group2):
                            new.append([newGroup1, rest[i]] + rest[:i] + rest[i + 1:])
                        
                        if group2:
                            # 处理除法
                            new.append([group1 / group2, rest[i]] + rest[:i] + rest[i + 1:])
                    
                    else:
                        new.append([group2, rest[i]] + rest[:i] + rest[i + 1:])
            
            q = new
        
        return False

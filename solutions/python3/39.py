
class Solution:
    # 定义一个求解组合和问题的类

    def combinationSum(self, candidates, target):
        # 初始化结果列表、栈以及候选数个数
        result, stack, n = [], [(0, [], 0)], len(candidates)
        
        while stack:  # 当栈不为空时，继续循环
            sum_val, tmp_list, right_index = stack.pop()  # 弹出栈顶元素
            
            for i in range(right_index, n):  # 从当前右边界开始遍历候选数列表
                if sum_val + candidates[i] < target: 
                    # 如果当前和加上下一个数小于目标值，则压入新状态到栈中
                    stack.append((sum_val + candidates[i], tmp_list + [candidates[i]], i))
                    
                elif sum_val + candidates[i] == target:
                    # 如果当前和等于目标值，找到一组解，将其加入结果列表
                    result.append(tmp_list + [candidates[i]])
        
        return result  # 返回所有满足条件的组合和列表

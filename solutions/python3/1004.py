
class Solution:
    # 定义一个类来解决问题
    
    def longestOnes(self, A: List[int], K: int) -> int:
        # 初始化零的位置列表，包括边界值
        zeros = [-1] + [i for i, c in enumerate(A) if not c] + [len(A)]
        # 结果变量初始化为0
        res = 0
        
        # 遍历零的位置列表，找到最大连续1的长度
        for j in range(K + 1, len(zeros)):
            res = max(res, zeros[j] - zeros[j - K - 1] - 1)
        
        # 返回结果或根据K和A的长度返回A的长度（为了处理特殊情况）
        return res or K and len(A)

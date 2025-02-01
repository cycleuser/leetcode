
class Solution:
    # 定义一个类来解决问题

    def numberOfArithmeticSlices(self, A):
        # 检查数组A长度是否小于3，如果是返回0
        if len(A) < 3:
            return 0
        
        # 在数组末尾添加一个无穷大的数以处理边界情况
        A.append(float("inf"))
        
        # 初始化变量：d为当前差值, l为差值起始位置, n为A的长度，res为结果计数器
        d, l, n, res = A[1] - A[0], 0, len(A), 0
        
        for i in range(2, n):
            # 如果当前元素与前一个元素的差值不等于d，则更新结果并重置d和l
            if d != A[i] - A[i - 1]:
                diff = i - l - 2
                if diff > 0:
                    res += diff * (diff + 1) // 2
                d, l = A[i] - A[i - 1], i - 1
        
        # 返回结果计数器res的值
        return res

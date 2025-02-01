
class Solution:
    # 定义一个类来解决数组加整数的问题

    def addToArrayForm(self, A, K):
        # 遍历数组A，从后向前逐位相加K，并处理进位
        for i in range(len(A))[::-1]:
            A[i], K = (A[i] + K) % 10, (A[i] + K) // 10
        
        # 如果K还有剩余部分，则将其转换为列表并添加到A的前面
        return [int(i) for i in str(K)] + A if K else A
